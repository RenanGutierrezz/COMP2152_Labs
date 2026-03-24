import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice: \n 1 - Rock\n 2 - Paper\n 3 - Scissor\n")

playerChoice = int(playerChoice)

if playerChoice <1 or playerChoice > 3:
  print("Error: Choice be between 1 and 3!")
else:
  computerChoice = random.randint(1,3)

  playerChoiceIndex = choices[playerChoice -1]
  computerChoiceIndex = choices[computerChoice -1]

  print("You chose: ", playerChoice)
  print("Computer chose: ", computerChoice)

  #Determine the user using if/elif/else
  if playerChoice == computerChoice:
    print("Its a tie!")
  elif playerChoice == 0 and  computerChoice == 2:
    print("Rock beats Scissor - You win!")
  elif playerChoice == 1 and computerC == 0:
    print("Paper beats Rock - You win!")
  elif playerChoice ==2 and computerChoice == 1:
    print("Scissors beats Paper - You win!")
  else:
    print("You lose!")
