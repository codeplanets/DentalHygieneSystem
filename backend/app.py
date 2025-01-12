from flask import Flask, request, jsonify, Response
import json
import cv2

app = Flask(__name__)

@app.route('/save_brushing_data', methods=['POST'])
def save_brushing_data():
    data = request.json
    # 데이터 저장 로직 추가
    return jsonify({"message": "Data saved successfully!"}), 200

@app.route('/video_feed')
def video_feed():
    return Response(generate_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_video_stream():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
