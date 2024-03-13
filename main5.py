import cv2
import face_recognition

# Load reference images and their encodings
known_faces = {
    
    "Isuru": face_recognition.face_encodings(face_recognition.load_image_file("p2.jpg"))[0],
    "Sithara": face_recognition.face_encodings(face_recognition.load_image_file("p12.jpg"))[0],
    # Add more persons as needed
}

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to RGB for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    
    if face_locations:
        # Encode the faces in the frame
        frame_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in the frame
        for face_encoding, (top, right, bottom, left) in zip(frame_encodings, face_locations):
            # Compare the face encoding with known faces
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            name = "Unknown"

            # Check if any known face matches
            for i, match in enumerate(matches):
                if match:
                    name = list(known_faces.keys())[i]
                    break

            # Display the name as alert
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # Draw rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
