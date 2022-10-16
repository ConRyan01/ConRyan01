import random

userWins = 0
computerWins = 0

options = ["rock","paper","scissors"]

while True:
    userInput = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        print('not a valid input')
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computerPick = options[random_number]
    print(f'Computer picked {computerPick}.')

    if userInput == "rock" and computerPick == "scissors":
        print("You Won!")
        userWins += 1

    elif userInput == "paper" and computerPick == "rock":
        print("You Won!")
        userWins += 1

    elif userInput == "scissors" and computerPick == "paper":
        print("You Won!")
        userWins += 1

    elif userInput == computerPick:
        print("Tie! Try again.")

    else:
        print('You Lost!')
        computerWins += 1

print(f'You won {userWins} time(s)! \nThe computer won {computerWins} time(s)!')
print("Goodbye!")
