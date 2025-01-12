import cv2
import requests
from brushing_guide import generate_brushing_guide

def start_video_processing():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        brushing_guide = generate_brushing_guide(frame)

        # 가이드 오버랩 및 서버에 데이터 전송
        overlay = create_guide_overlay(frame, brushing_guide)
        combined_frame = cv2.addWeighted(frame, 0.7, overlay, 0.3, 0)

        # 서버에 데이터 전송
        requests.post('http://localhost:5000/save_brushing_data', json={"guide": brushing_guide})

        cv2.imshow('Brushing Guide', combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    