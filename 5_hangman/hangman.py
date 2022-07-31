import random
from words import words
import string

# to ensure chossen word does not have '-' 
def get_valid_word(words):
    word = random.choice(words) # randomly choose word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()      # keeps track what user has guessed

    lives = 6

    #getting user input 
    while (len(word_letters) > 0) and (lives > 0):
        #here we need to tell the user some info

        # tell user what letters used
        # ' .join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ' + str(lives) + ' lives left.')
        print("You have used these letters: " + ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: " + ''.join(word_list))

        #user input and storing that input
        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:  #if letter is in alphabet but is not used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:         #if letter is in the word
                word_letters.remove(user_letter)
            else: 
                lives = lives - 1                   #takes away life
                print('You letter ' + user_letter + ' is not in the word')
        elif user_letter in used_letters:
            print("You have already used that character. Try again silly")
        else:
            print("Invalid character. Try again weirdo")

#gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died! The word was ' + word)
    else: 
        print('Congrats! You guessed the word ' + word + ' correctly!!')

print(hangman())