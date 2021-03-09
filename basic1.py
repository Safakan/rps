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
elif choice_p1 == choice_p2:
	print ("It's a tie!")
else:
    print ("Player 2 wins!")


#this one works when each player follow the rules.
#Tie situation and player 1's winning options are defined. In any other situation player 2 wins.
#But if players don't enter rock, paper, or scissors; still player 2 wins because that falls into else category
#I should learn a way to force choices between these 3!
