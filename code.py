import random
import time
import numpy as np
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

FINGER_TIPS_LIST = {8, 12, 16, 20} #index, middle, ring, pinky
MOVE_MAP = {"0000": "Earth", "1111": "Wood", "1010": "Metal", "1001": "Fire", "0111": "Water"}

def get_move(hand_landmark):
    state = ""
    for tip in FINGER_TIPS_LIST:
        if hand_landmark[tip].y < hand_landmark[tip - 2].y: #check other fingers (if finger tip y < finger base y then finger is open)
            state += "1"                                    #coordintes are flipped so y increases when going down
        else:
            state += "0"
    return MOVE_MAP.get(state, "N/A") #return N/A if state is not in MOVE_MAP

def pick_winner(player_move):
    computer_move = random.choice(["Earth", "Wood", "Metal", "Fire", "Water"])
    if player_move == computer_move:
        return 0, computer_move #draw
    elif (player_move == "Metal" and computer_move in ["Wood", "Earth"]) or \
        (player_move == "Wood" and computer_move in ["Earth", "Water"]) or \
        (player_move == "Earth" and computer_move in ["Water", "Fire"]) or \
        (player_move == "Water" and computer_move in ["Fire", "Metal"]) or \
        (player_move == "Fire" and computer_move in ["Metal", "Wood"]):
        return 1, computer_move #player wins
    else:
        return -1, computer_move #player loses

#put text on screen
def screen_text(frame, text, position, color):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1)

def start_capture():
    options = vision.HandLandmarkerOptions(
        base_options = python.BaseOptions(model_asset_path="hand_landmarker.task"), 
        running_mode = vision.RunningMode.VIDEO, 
        num_hands = 1,
        min_hand_detection_confidence = 0.4,
        min_tracking_confidence = 0.7)

    landmarker = vision.HandLandmarker.create_from_options(options)

    capture = cv2.VideoCapture(0) #0 is default camera
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    start_time = time.time()

    while True:
        ready, frame = capture.read()
                                        
        if not ready:
            break

        frame = cv2.flip(frame, 1)
        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=color_frame)

        timestamp_ms = int((time.time() - start_time) * 1000)
        hand_landmarker_result = landmarker.detect_for_video(mp_image, timestamp_ms)
        if hand_landmarker_result.hand_landmarks:
            hand_on_screen = hand_landmarker_result.hand_landmarks[0]
        else: 
            hand_on_screen = None

        if hand_on_screen:
            current_move = get_move(hand_on_screen)
        else:
            current_move =  "N/A"

        height, width, _ = frame.shape #_ is used to ignore third value in the shape tuple
        for on_screen_hand in hand_landmarker_result.hand_landmarks:
            for point in on_screen_hand:
                cv2.circle(frame, (int(point.x * width), int(point.y * height)), 5, (0, 255, 255), -1)
            screen_text(frame, f"Move: {current_move}", (10, 50), (0, 0, 0))

        if current_move != "N/A":
            game_result, computer_move = pick_winner(current_move)
            if game_result == 1:
                screen_text(frame, f"Your Move: {current_move} | Computer Move: {computer_move} | You Win!", (125, 500), (0, 255, 0))
            elif game_result == 0:
                screen_text(frame, f"Your Move: {current_move} | Computer Move: {computer_move} | It's a Draw!", (125, 500), (0, 255, 255))
            elif game_result == -1:
                screen_text(frame, f"Your Move: {current_move} | Computer Move: {computer_move} | You Lose!", (125, 500), (0, 0, 255))
        
        cv2.imshow("RPS", frame)

        if cv2.waitKey(1) == 27: #27 is ascii for esc key
            break   

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_capture()
