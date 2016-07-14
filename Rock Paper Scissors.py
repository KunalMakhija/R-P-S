#Program to simulate a rock paper scissors game vs the computer				
				
from random import randint		
from time import sleep
import ctypes
				
options = ["R","P","S"]				
LOSS_MESSAGE = "You lost!"				
WIN_MESSAGE = "You won!"				

def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
				
def decide_winner(user_choice, computer_choice):				
    print ("You selected %s" % user_choice)				
    print ("Computer selecting...")				
    sleep(1)				
    print ("Your opponent selected %s" % computer_choice)				
    user_choice_index = options.index(user_choice)				
    computer_choice_index = options.index(computer_choice)				
    if user_choice_index == computer_choice_index:				
        print ("Tie, go again")				
    elif user_choice_index == 0 and computer_choice_index == 2:				
        Mbox ("Outcome","You won!", 1)				
    elif user_choice_index == 1 and computer_choice_index == 0:				
        Mbox ("Outcome","You won!", 1)				
    elif user_choice_index == 2 and computer_choice_index == 1:				
        Mbox ("Outcome","You won!", 1)				
    elif user_choice_index > 2:				
        print ("Choose either Rock, Paper, or Scissors!")				
        return				
    else:				
        Mbox ("Outcome","You lost!", 1)				
				
def play_RPS():				
    print ("Let's play Rock, Paper, Scissors!")				
    user_choice = input("Select R for Rock, P for Paper, or S for Scissors: ")				
    sleep(1)				
    user_choice = user_choice.upper()				
    computer_choice = options[randint(0,len(options)-1)]				
    decide_winner(user_choice,computer_choice)
    playagain()

def playagain():
    replay = input("Want to play again? ").lower()
    if replay == "yes":
        print ('')
        play_RPS()
    elif replay != "yes":
        print ('')
        print ('')
        print ("Ight")
        quit()
				
play_RPS()				
