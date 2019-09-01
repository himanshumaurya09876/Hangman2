import random
from time import sleep
from os import system, name


def clear():
    #for windows
    if name == "nt":
        _ = system('cls')
    #for linux and mac use -- name == 'posix'
    else:
        _ = system("clear")


choice = "y"
score = [0, 0]
round = 1

while choice == "y":
    for i in range(1, 3):
        clear()
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::Welcome to Hangman:::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Instructions:")
        print("-->There will be two players- 1 and 2.")
        print("-->One of the players will set a word/number/or anything secret and then another player will have to guess that secret.")
        print("-->Players can provide hint.And also they can set maximum number of chances to be given to opponent.")
        print("-->If a Player wins then his/her score will be incremented by 1.")
        print("-->If a Player loses then his/her score will be decremented by 1.So score can be negative, be careful!")
        print("\n**********************::::::::::: Round- " + str(round) + " :::::::::::**********************")
        print("\nPlayer-" + str(i) + "! You have to give a secret to Player-" + str(3-i))
        word = input("Enter a word/number/or anything secret: ")
        while word == "":
            word = list(word)
            word.clear()
            word = "".join(input("Please enter a valid word/number/or anything secret: "))
        hint = input("Any hint for Player-" + str(3-i) + "(If no then enter- no): ")
        while hint == "":
            hint = list(hint)
            hint.clear()
            hint = "".join(input("Please enter a valid hint for Player-" + str(3-i) + "(If no then enter- no): "))
        chances = input("Enter, maximum how many times Player-" + str(3-i) + " can make incorrect guesses: ")
        while not(chances.isdecimal()):
            chances = list(chances)
            chances.clear()
            chances = "".join(input("Please enter a valid number for, maximum how many times Player-" + str(3-i) + " can make incorrect guesses: "))
        clear()
        print("\n:::::::::::::::::::::::::::::::::::::::::::::::::Welcome to Hangman:::::::::::::::::::::::::::::::::::::::::::::::::")
        print("Instructions:")
        print("-->There will be two players- 1 and 2.")
        print("-->One of the players will set a word/number/or anything secret and then another player will have to guess that secret.")
        print("-->Players can provide hint.And also they can set maximum number of chances to be given to opponent.")
        print("-->If a Player wins then his/her score will be incremented by 1.")
        print("-->If a Player loses then his/her score will be decremented by 1.So score can be negative, be careful!")
        print("\n**********************::::::::::: Round- " + str(round) + " :::::::::::**********************")
        sleep(1)
        print("\nPlayer-" + str(3-i) + "! It's your turn to guess the secret word/code.")
        print("Guess the word: ", end="")
        guess = ""
        for letter in word:
            if word.index(letter) == len(word) - 1:
                guess += letter
            else:
                guess += "*"
        print(guess)
        print("Hint: " + hint)
        print("You can have only " + chances + " incorrect guesses.So be careful!")
        if int(chances) == 0:
            incorrect = -1
        else:
            incorrect = 0
        tag = ""
        while incorrect < int(chances):
            ans = input("Guess a letter/code: ")
            if ans != "":
                if ans in guess:
                    print("Already guessed! Please guess another letter.....")
                    continue
                elif ans in word:
                    print("Correct guess! Keep going......")
                    for j in range(len(word)):
                        guess = list(guess)
                        if word[j] == ans:
                            guess[j] = word[j]
                        guess = "".join(guess)
                    print("\nWord/code guessed till now: " + guess)
                    if guess == word:
                        tag = "completed"
                        break
                else:
                    print("Incorrect guess! Try again......")
                    incorrect += 1
                    print("Hangman status: ", end=" ")
                    if incorrect == int(chances) - 1:
                        print(" :(    -->You are going to be hanged...")
                    elif incorrect == int(chances):
                        print("|")
                        print("                 |      -->You died!")
                        print("                 O")
                        print("                 |")
                        print("                /|\\")
                        print("               | | |")
                        print("                 |")
                        print("                / \\")
                        print("               |   |")
                    else:
                        print(" :)    -->Still alive................")
                    print("Number of chances left: " + str(int(chances) - incorrect))
                    print("\nWord/code guessed till now: " + guess)
            else:
                print("Invalid guess! Please, guess a valid letter/code.........")

        print("The word/code was: " + word)
        if tag == "completed":
            score[3 - i - 1] += 1
            print("Congratulations! You win this round. You guessed the complete word/code................")
            print("Your current score is: " + str(score[3 - i - 1]))
        else:
            score[3 - i - 1] -= 1
            print("Sorry! You lost this round................")
            print("Your current score is: " + str(score[3 - i - 1]))
        input()
    choice = input("If you want to play next round then press- y, otherwise any key: ")
    round += 1


print("Score of Player-1 is: " + str(score[0]))
print("Score of Player-2 is: " +str(score[1]))

if score[0] > score[1]:
    print("Player-1 wins the game!!!!!!!!!!!!!")
elif score[0] < score[1]:
    print("Player-2 wins the game!!!!!!!!!!!!!")
else:
    print("There is a tie, both the Players win the game............")
    print("Play again to check who is more powerful.....")