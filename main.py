# This code simulates a guessing game between the user and the program.
import random  # This module is required for the random number generator.

# Initializing values needed for later.
wins = 0
guesses_total = 0
guesses_taken = 0
random_number = random.randint(1, 10)

print('Play (y/n?):', end=' ')  # Asks if the user wants to play.
choice = input()

while True:  # Main gameplay loop that keeps the game going until the user quits.
  while choice == 'y' or choice == 'Y':
    for guesses_taken in range(5):  # Gameplay loop for a single round with up to 5 guesses allowed.
      while True:  # Validates user input to prevent a fatal crash.
        try:
          player_guess = int(input("\tEnter an integer from 1 to 10: "))
        except ValueError:
          print("\t\tPlease enter a valid integer.")  # User is perpetually prompted until a valid input.
          continue
        else:
          break  # Valid input allows to break out from this loop.

        if player_guess == random_number:  # Condition to exit the input loop. The player wins.
          break
        else:
          print('\t\tIncorrect. Please guess again.'
              )  # Loop is replayed until 5 losses or the game is won.

      if player_guess == random_number:  # Displays a winning message and adds to the win count.
        print('\t\tCongratulations! You guessed right in this number of tries for this round:', guesses_taken + 1)
        wins += 1
        guesses_total = guesses_total + guesses_taken + 1  # Registers total guesses. The plus one is
                                                           # because the count started from 0.
    
    print('Play again? (y/n):', end=' ')  # Asks if the user wishes to play another round.
    choice = input()
    if choice == 'y' or choice == 'Y':  # Main gameplay loop restarts.
      continue
    elif choice == 'n' or choice == 'N':  # Main gameplay loop is exited.
      break
    else:  # Prompts for valid input if inappropriate input was detected.
      print('\tPlease input y or n:', end=' ')
      choice = input()

  if choice == 'n' or choice == 'N':  # Choice conditional for the gameplay loop (at the outermost layer).
    print('See you again next time!')
    break
  else:
    print('Please input y or n:', end=' ')  # Prompts for valid input if inappropriate input was detected.
    choice = input()

print('\tTotal guesses:', guesses_total)  # Displays game statistics.
print('\tTotal wins:', wins)
if guesses_total > 0:  # This condition prevents a crash caused by dividing by zero.
  print('\tSuccess rate: ', round(wins / guesses_total * 100, 2), '%', sep='')
  # Success rate is displayed as a percentage and rounded up to 2 decimal places.
