import random
print("Welcome to Rock, Paper and Scissors game.")
print("Read the Carefully:")
print("R for Rock")
print("P for Paper")
print("S for scissors")

while True:
    user_action = input("Enter a choice (R, P, S): ")
    if user_action in ("R"):
        user_action = "Rock"
    elif user_action in ("P"):
        user_action = "Paper"
    elif user_action in ("S"):
        user_action = "Scissors"
    else:
        print("invalid entry, try again.")

    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer ({user_action}): CPU ({computer_action}).\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        pass
    
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break

