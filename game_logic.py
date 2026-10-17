import random

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
