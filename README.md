# Real-time Face Recognition using OpenCV and face_recognition

This Python script demonstrates real-time face recognition using OpenCV and the face_recognition library. It utilizes the webcam to capture frames, detects faces in the frames, and compares them with a set of known faces to recognize individuals. 

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- OpenCV (`pip install opencv-python`)
- face_recognition (`pip install face_recognition`)

Additionally, you need to have a webcam connected to your system.

## Usage

1. Clone this repository or download the script `face_recognition.py`.
2. Place the images of known faces in the same directory as the script. Ensure the image filenames correspond to the names used in the `known_faces` dictionary within the script.
3. Run the script using Python:

    ```bash
    python face_recognition.py
    ```

4. The script will open up your webcam and start recognizing faces in real-time. When a known face is detected, it will display the name associated with that face. Press 'q' to exit the program.

## Configuration

- `known_faces`: This dictionary contains the names of known individuals as keys and their corresponding face encodings as values. Add more entries as needed for additional individuals.

## Dependencies

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- [face_recognition](https://github.com/ageitgey/face_recognition): A simple face recognition library built on top of dlib.

---
