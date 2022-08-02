import time
import random

def play():
    user = input("Choose your fighter \n'r' for rock, 'p' for paper, 's' for scissors \n").lower()
    computer = random.choice(['r', 'p', 's'])
    time.sleep(0.8)

    if user == computer:
        return "It's a tie ! PLAY AGAIN!"

    if is_win(user, computer):
        return "YES QUEEN YOU WON!"
    
    return "Sorry you lost D:"

    
    
def is_win(player, opponent):
# return True if player wins
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'): 
        return True

print(play())