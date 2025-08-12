import random
choice = ["snake", "water", "gun"]

def result(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You Win"
    else:
        return "Computer Wins"

def play():
    print("\n🎮 Choose Your Option:")
    print("  0️⃣  - Snake 🐍")
    print("  1️⃣  - Water 💧")
    print("  2️⃣  - Gun 🔫")
    user = int(input("Enter your choice (0/1/2): "))
    if(user == 0 or user == 1 or user == 2):
        print("Your choice:     ",choice[user])
        computer = random.randint(0, 2)
        print("Computer choice: ",choice[computer])
        print(result(choice[user], choice[computer]))
    else:
        print("Invalid Choice! Please enter 0, 1, or 2.")

while(True):
    print()
    start = input("Do you want to play (y/n): ")
    if(start == 'y'):
        play()
    elif(start == 'n'):
        print("Thanks for playing...")
        break
    else:
        print("Please enter 'y' or 'n'.")



