import random
import time
#This code change welcomes the player to the game and asks them to enter their name to be displayed and greeted
print("\nWelcome to the Hangman Game!\n")
name = input("Enter your name: ")
print("Hello + name + "! Good Luck!")
time.sleep(2)
print("The game is about to start!\n Lets Play!")
time.sleep(3)
 # This change lists the words that are to be guessed in the game but does not display them to the player but instead displays a blank space per each letterof the listed words
def main():
  global count
  global display
  global word
  global already_guessed
  global length
  global play_game
  words_to_guess = ["python","application","development","code","github","information","security","assurance","kennesaw","state","college"]
  word = random.choice(words_to_guess)
  length = len(word)
  count = 0
  display = '_' * length
  already_guessed = []
  play_game = ""
  #This change asks the player if they wish to play again if they play again and depending on their answer will restart the game or end it and thank them for playing
def play_loop():
  global play_game
  play_game = input("Do you want to play again? y =yes, n = no \n")
  while play_game not in ["y","n","Y","N"]:
    play_game = input("Do you want to play again? y = yes, n = no \n")
  if play_game == "y":
    main()
   elif play_game =="n":
    print("Thanks for playing! Come back soon!")
    exit()
    # This asks the player to enter their guess and determines if it is an accepted input
def hangman():
      global count 
      global display
      global word
      global already_guessed
      global play_game
      limit = 5
      guess = input("This is your word: " + display + "Enter your guess:\n")
      guess = guess.strip()
      if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
   # This change will count the wrong guess and determine if it is wrong or not as well as ask the player to try another letter   
      elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
      
      elif guess in already_guessed:
        print("Try another letter.\n")
 #This change displays the image of the hangman if an incorrect guess is given     
      else:
        count += 1
      if count == 1:
        time.sleep(1)
        print(" ______ \n"
              "|  \n"
              "|  \n"
              "|  \n"
              "|  \n"
              "|  \n"
              "|  \n"
              "_|___  \n"
        print("Wrong. " +str(limit - count) + "Guesses remaining\n")
              
      elif
              
