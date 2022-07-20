import random
import time

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
    
