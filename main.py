import time
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from game_logic import pick_winner
from hand_sign import get_move

#put text on screen
def screen_text(frame, text, position, color):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1.25, color, 2)

def start_capture():
    options = vision.HandLandmarkerOptions(
        base_options = python.BaseOptions(model_asset_path="hand_landmarker.task"), 
        running_mode = vision.RunningMode.VIDEO, 
        num_hands = 1,
        min_hand_detection_confidence = 0.7, #higher value = less false detection
        min_hand_presence_confidence = 0.7)

    landmarker = vision.HandLandmarker.create_from_options(options)

    capture = cv2.VideoCapture(0) #0 is default camera
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    start_time = time.time()
    move_wait_time = 30 #time to wait for player to hold their move to prevent premature move detection
                        #camera framerate is 30fps so 30 frames is 1 second
    game_state = "waiting" #3 states: waiting, playing, result

    while True:
        ready, frame = capture.read() #ready checks if camera is available, frame is the capture window
                                        
        if not ready:
            break

        frame = cv2.flip(frame, 1) #1 flips the camera horizontally
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) #switch from BGR to RGB for mediapipe

        timestamp_ms = int((time.time() - start_time) * 1000)
        hand_landmarker_result = landmarker.detect_for_video(mp_image, timestamp_ms)
        
        if hand_landmarker_result.hand_landmarks: 
            detected_hand = hand_landmarker_result.hand_landmarks[0]
        else: 
            detected_hand = None

        if detected_hand:
            current_move = get_move(detected_hand) #get move from landmarks on the detected hand
        else:
            current_move =  "N/A"

        height, width, _ = frame.shape #_ is used to ignore third value in the shape tuple
        for on_screen_hand in hand_landmarker_result.hand_landmarks:
            for point in on_screen_hand:
                cv2.circle(frame, (int(point.x * width), int(point.y * height)), 5, (0, 255, 255), -1)
            if game_state != "result":
                screen_text(frame, f"Move: {current_move}", (10, 50), (0, 0, 0)) #player can preview their move before the game starts or while playing

        
        if game_state == "waiting":
            screen_text(frame, "Press Space to start", (280, 500), (0, 200, 255))

        if game_state == "playing":
            if current_move != "N/A":
                move_wait_time -= 1
                if move_wait_time <= 0:
                    game_result, computer_move = pick_winner(current_move)
                    played_move = current_move
                    game_state = "result"
                    
        if game_state == "result":
            screen_text(frame, "Game Over! Press Space to play again", (150, 475), (255, 255, 255))
            if game_result == 1:
                screen_text(frame, f"Your Move: {played_move} | Computer Move: {computer_move} | You Win!", (30, 525), (0, 255, 0))
            elif game_result == 0:
                screen_text(frame, f"Your Move: {played_move} | Computer Move: {computer_move} | It's a Draw!", (30, 525), (0, 255, 255))
            elif game_result == -1:
                screen_text(frame, f"Your Move: {played_move} | Computer Move: {computer_move} | You Lose!", (30, 525), (0, 0, 255))

        cv2.imshow("Wuxing Rock Paper Scissors", frame)

        special_key = cv2.waitKey(1) #wait 1ms for a key press and return the ascii value of the key pressed, 0ms will break the loop if no key is pressed
        if special_key == 27: #27 is ascii for esc key
            break   #exit the game if esc key is pressed
        
        if (game_state == "waiting" or game_state == "result") and special_key == 32: #32 is ascii for space key
            game_state = "playing"
            move_wait_time = 30 #reset move_wait_time for next round
 
    capture.release()
    cv2.destroyAllWindows()

def main():
    start_capture()

if __name__ == "__main__":
    main()