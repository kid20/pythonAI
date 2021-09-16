#pip install mediapipe opencv-python
#install dependencies
import mediapipe as mp
import cv2


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

#Drawing connections
mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        # pang kulay
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Mag dedetect
        results = holistic.process(image)
        # iprint ang resulta



        # baguhin ang kulay
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 1. Iguhit ang landmarks sa mukha
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1))

        # 2. Kanang Kamay
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2))

        # 3. Kaliwang Kamay
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2))

        # 4. Pose Detect
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

        cv2.imshow('Raw Webcam Feed- Press Q to quit', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
