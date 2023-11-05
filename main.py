import random
import sys
from colorama import Fore

from colorama import  Back, Style


def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        words = [word.strip() for word in file.readlines()]
        return random.choice(words)

def printGuessColors(guess,answer):
    for i in range(len(guess)):
        if len(guess)== 5:
            print(letterColor(i,guess,answer))
        else:
            print("choose a 5 letter word")



def main():
    choice = input("Easy or hard mode?: ")
    choice.lower()
    if choice == "easy" or choice == "easy mode":
        print('You have chosen Easy mode you have 6 tries to guess the answer')
    elif choice == "hard" or choice == "hard mode":
        print('You have chosen hard mode you have 5 tries to guess the answer')
    else:
        print('it therefore goes to Easy mode')
    answer = getRandomWord()
    #print(answer)
    guess=input(Fore.BLACK + "Enter a 5 letter guess?\n") 
    guess = guess.lower()
    counter = 1
    if choice == "easy" or choice == "easy mode":
        while counter <7:
            if counter == 6:
                printGuessColors(guess,answer)
                print(f"You lost. The answer was {answer}.")
                break
            elif guess == answer:  
                (printGuessColors(guess,answer))
                print(f"You Won! That took {counter} guess(es).")       
                break
            
            elif guess != answer:
                (printGuessColors(guess,answer))
                guess=input(Fore.BLACK + "Enter a 5 letter guess?\n")
                guess = guess.lower()

            counter += 1

    if choice == "hard" or choice == "hard mode":
        while counter <6:
            if counter == 5:
                printGuessColors(guess,answer)
                print(f"You lost. The answer was {answer}.")
                break
            elif guess == answer:  
                (printGuessColors(guess,answer))
                print(f"You Won! That took {counter} guess(es).")       
                break
            
            elif guess != answer:
                (printGuessColors(guess,answer))
                guess=input(Fore.BLACK + "Enter a 5 letter guess?\n")
                guess = guess.lower()

            counter += 1
          
        


def letterColor(index, guess, answer):
    if len(guess)!=5:
        return("choose a 5")
    elif len(guess) == 5:
        if guess[index]==answer[index]:
            return (Fore.GREEN + guess[index])
        elif guess[index] in answer:
            return (Fore.YELLOW + guess[index])
        elif guess[index] not in answer:
            return (Fore.RED + guess[index])

(main())
