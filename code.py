import mediapipe
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np

def start_capture():
    #drawing_utils = mediapipe.tasks.vision.drawing_utils
    #hands = mediapipe.tasks.vision.HandLandmarkerOptions(base_options=python.BaseOptions(model_path="hand_landmarker.task"),
     #                                    running_mode=mediapipe.tasks.vision.RunningMode.LIVE_STREAM,
      #                                   num_hands=2,
       #                                  min_hand_detection_confidence=0.7,
        #                                 min_tracking_confidence=0.4, 
         #                                result_callback=None)


    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()

        #results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #if results.multi_hand_landmarks:
         #   for hand_landmarks in results.multi_hand_landmarks:
          #      drawing_utils.draw_landmarks(frame, hand_landmarks, hands.HAND_CONNECTIONS, 
           #                                  drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=4, circle_radius=4), 
            #                                 drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=7, circle_radius=2))
        
        cv2.imshow("RPS", frame)

        if cv2.waitKey(1) == 27: # 27 is the ASCII code for the Esc key
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_capture()
