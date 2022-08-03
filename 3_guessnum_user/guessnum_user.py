import random

def computer_guess(x): 
# set low and high variables so we can change the upper and lower bounds of what number comp is guessing

    low = 1
    high = x
    feedback = ""
    while feedback != "c":
# computer cant randint if low and high are equal (but if they are equal, computer narrowed number to answer)
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high since low = high
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = (guess - 1)
        elif feedback == 'l':
            low = (guess + 1)
        
    print(f"Yay! The computer guessesd your number, {guess}, correctly!")


x = int(input("Enter a number to range from 1 to __ : "))
computer_guess(x)