#Can be played here
print("Let's play hangman!")

import random

def get_word():
    words = ['HELLO', 'AUTHENTIC', 'LIGHT', 'KERNEL', 'INTEREST', 'COMPUTER', 'RADIANT','FOOD']
    return random.choice(words)


def play_game():
    word = get_word()
    alpha = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    letters_guessed = []
    count_tries = 6
    guessed = False

    print("The word you are guessing has", len(word), "letters.")
    print(len(word) * '_')
    while guessed == False and count_tries > 0:
        print("You have " + str(count_tries) + " tries left.")
        guess = input("Guess a letter or word: ").upper()

        if len(guess) == 1:
            if guess not in alpha:
                print("Not a valid guess!")
            elif guessed in letters_guessed:
                print("That letter was already guessed.")
            elif guess not in word:
                print("Nah! That is not in the word.")
                letters_guessed.append(guess)
                count_tries -= 1
            elif guess in word:
                print("You're smart! This letter is right.")
                letters_guessed.append(guess)
            else:
                print("I can't understand!")
        elif len(guess) == len(word):
            if guess == word:
                print("Wow! You did it! ^o^")
                guessed = True
            else:
                print("Maybe next time!")
                count_tries -=1
        else:
            print("The length does not look right...")

        status = ""
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += "_"
                print(status)
        if status == word:
            print("You guessed the word!")
            guessed = True
        elif count_tries == 0:
            print("Whoops! You are out of tries 😢")

play_game()
