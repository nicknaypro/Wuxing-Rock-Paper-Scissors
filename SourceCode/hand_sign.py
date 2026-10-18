FINGER_TIPS_LIST = {8, 12, 16, 20} #index, middle, ring, pinky
MOVE_MAP = {"0000": "Earth", "1111": "Wood", "1010": "Metal", "1001": "Fire", "0111": "Water"}

def get_move(hand_landmark):
    state = ""
    for tip in FINGER_TIPS_LIST:
        if hand_landmark[tip].y < hand_landmark[tip - 2].y: #check fingers (if finger tip y < finger base y then finger is open)
            state += "1"                                    #coordintes are flipped so y increases when going down
        else:
            state += "0"
    return MOVE_MAP.get(state, "N/A") #return N/A if state is not in MOVE_MAP
