print ("WELCOME TO THE WORLDS MOST BASIC ROCK PAPER SCISSORS GAME!")
print ("(Press Enter)")
input()

print ("Now, you are going to take turns! (Press Enter)")
input()

print ("GO AHEAD PLAYER 1, THINK TWICE AND BE WISE!")
print ("rock! paper! scissors!")
choice_p1 = input("SELECT! ")

print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")
print ("NO PEAKING!")

print ("Player 2, it's all up to you now!")
print ("Rock! Paper! Scissors!")
choice_p2 = input("SELECT! ")

print ("Enter for the result! (drum roll please)")
input ()

print (f"{choice_p1} VS. {choice_p2}")

# Draws or not cleared
# only works when rules are followed

if choice_p1 == "rock" and choice_p2 != "paper":
    print ("Player 1 wins!")
elif choice_p1 == "paper" and choice_p2 != "scissors":
    print ("Player 1 wins!")
elif choice_p1 == "scissors" and choice_p2 != "rock":
    print ("Player 1 wins!")
else:
    print ("Player 2 wins!")

