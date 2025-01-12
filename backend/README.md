# Dental Hygiene System

This project assists children with their teeth brushing by overlaying guidance on their actions captured through a camera.

## Requirements

- Flask
- OpenCV
- some-llm-library (replace with actual library)

## Running the Project

1. Install the required packages:
```
pip install -r requirements.txt
```

2. Start the Flask server:
```
python app.py
```

3. Start the video processing:
```
python video_processing.py
```

## Functionality

- Captures video from the camera.
- Overlays brushing guidance on the video.
- Sends brushing data to the server for storage.