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

model = YOLO('weights/best.pt')
video_path = None
use_live_camera = False
detected_counts = {"empty": 0, "occupied": 0}


def allowed_file(filename, allowed_exts):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts


@app.route('/', methods=['GET', 'POST'])
def index():
    global video_path, use_live_camera, detected_counts
    result = None
    is_video = False
    use_live_camera = False
    detected_counts = {"empty": 0, "occupied": 0}

    if request.method == 'POST':
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
                boxes = results[0].boxes
                cls = boxes.cls.cpu().numpy()
                empty = int(np.sum(cls == 0))
                occupied = int(np.sum(cls == 1))

                annotated = results[0].plot()
                result_img = os.path.join(app.config['UPLOAD_FOLDER'], f"result_{filename}")
                cv2.imwrite(result_img, annotated)

                result = {
                    'image': f"result_{filename}",
                    'empty': empty,
                    'occupied': occupied
                }

    return render_template('index.html', result=result, is_video=is_video, is_live=use_live_camera,
                           count=detected_counts)


@app.route('/video_feed')
def video_feed():
    if use_live_camera:
        return Response(generate_frames_live(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(generate_frames_video(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_frames_video():
    global detected_counts
    cap = cv2.VideoCapture(video_path)
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        cls = results[0].boxes.cls.cpu().numpy()
        detected_counts["empty"] = int(np.sum(cls == 0))
        detected_counts["occupied"] = int(np.sum(cls == 1))

        annotated = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()


def generate_frames_live():
    global detected_counts
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        cls = results[0].boxes.cls.cpu().numpy()
        detected_counts["empty"] = int(np.sum(cls == 0))
        detected_counts["occupied"] = int(np.sum(cls == 1))

        annotated = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()


if __name__ == '__main__':
    app.run(debug=True)
