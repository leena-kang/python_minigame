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

    #getting user input 
    while len(word_letters) > 0:
        #here we need to tell the user some info

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:  #if letter is in alphabet but is not used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:         #if letter is in the word
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character. Try again silly")
        else:
            print("Invalid character. Try again weirdo")

#gets here when len(word_letters) == 0
