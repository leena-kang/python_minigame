import random

def play():
    user = input("Choose your fighter \n'r' for rock, 'p' for paper, 's' for scissors \n").lower()
    computer = random.choice(['r', 'p', 's'])

    while user == computer:
        print("It's a tie ! PLAY AGAIN!")
        user = input("Choose your fighter \n'r' for rock, 'p' for paper, 's' for scissors \n").lower()
    computer = random.choice(['r', 'p', 's'])

    if is_win(user, computer):
        return "YES QUEEN YOU WON!"
    
    return "Sorry you lost D:"

    
    
def is_win(player, opponent):
# return True if player wins
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'): 
        return True

print(play())