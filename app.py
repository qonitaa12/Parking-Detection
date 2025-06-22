from flask import Flask, render_template, request, Response, redirect, url_for
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from ultralytics import YOLO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_IMAGE = {'png', 'jpg', 'jpeg'}
ALLOWED_VIDEO = {'mp4', 'avi', 'mov'}

# Load kedua model
model_mobil = YOLO('weights/best.pt')
model_motor = YOLO('weights/best_motor.pt')

video_path = None
use_live_camera = False
detected_counts = {"empty": 0, "occupied": 0}
selected_mode = "mobil"  # default

def allowed_file(filename, allowed_exts):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts

def get_model(mode):
    return model_motor if mode == "motor" else model_mobil

@app.route('/', methods=['GET', 'POST'])
def index():
    global video_path, use_live_camera, detected_counts, selected_mode
    result = None
    is_video = False
    use_live_camera = False
    detected_counts = {"empty": 0, "occupied": 0}
    selected_mode = request.form.get("mode", "mobil")

    if request.method == 'POST':
        model = get_model(selected_mode)

        if 'live' in request.form:
            use_live_camera = True
            is_video = True

        elif 'finish' in request.form:
            use_live_camera = False
            return redirect(url_for('index'))

        else:
            file = request.files['image']
            filename = secure_filename(file.filename)
            ext = filename.rsplit('.', 1)[1].lower()
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            if allowed_file(filename, ALLOWED_VIDEO):
                video_path = save_path
                is_video = True
            elif allowed_file(filename, ALLOWED_IMAGE):
                results = model(save_path)
                cls = results[0].boxes.cls.cpu().numpy()

                if selected_mode == "motor":
                    occupied = int(np.sum(cls == 0))  # only one class: motorcycle
                    empty = 0
                else:
                    empty = int(np.sum(cls == 0))  # class 0: empty
                    occupied = int(np.sum(cls == 1))  # class 1: occupied

                annotated = results[0].plot()
                result_img = os.path.join(app.config['UPLOAD_FOLDER'], f"result_{filename}")
                cv2.imwrite(result_img, annotated)

                result = {
                    'image': f"result_{filename}",
                    'empty': empty,
                    'occupied': occupied
                }

    return render_template('index.html', result=result, is_video=is_video, is_live=use_live_camera,
                           count=detected_counts, selected_mode=selected_mode)

@app.route('/video_feed')
def video_feed():
    model = get_model(selected_mode)
    if use_live_camera:
        return Response(generate_frames_live(model), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(generate_frames_video(model), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames_video(model):
    global detected_counts
    cap = cv2.VideoCapture(video_path)
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        cls = results[0].boxes.cls.cpu().numpy()

        if selected_mode == "motor":
            detected_counts["occupied"] = int(np.sum(cls == 0))
            detected_counts["empty"] = 0
        else:
            detected_counts["empty"] = int(np.sum(cls == 0))
            detected_counts["occupied"] = int(np.sum(cls == 1))

        annotated = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

def generate_frames_live(model):
    global detected_counts
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        cls = results[0].boxes.cls.cpu().numpy()

        if selected_mode == "motor":
            detected_counts["occupied"] = int(np.sum(cls == 0))
            detected_counts["empty"] = 0
        else:
            detected_counts["empty"] = int(np.sum(cls == 0))
            detected_counts["occupied"] = int(np.sum(cls == 1))

        annotated = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

if __name__ == '__main__':
    app.run(debug=True)
