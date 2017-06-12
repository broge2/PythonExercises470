def play(choice):
    '''Plays a round of rock, paper, scissors...and wins'''
    valid_options = ("rock", "paper", "scissors")
    if choice in valid_options:
        if choice == "rock":
            return "paper" #paper beats rock
        elif choice == "scissors":
            return "rock" #rock beats scissors
        elif choice == "paper":
            return "scissors" #scissors beats paper
    else:
        return "That's not a valid option, cheater."
        
user_choice = input("Rock, Paper, Scissors: ").lower()
print(play(user_choice))