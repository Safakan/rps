#lets build XOX board in terminal
# I need lists, nested ones... 
# Design:
# => create a list with three values / I used range instead
# => use nested list comprehensions with conditionals to change the values, and to triple it
# => use "end" keyword argument in print function to line up those lists

#EMPTY BOARD
empty_board = [["*" for val in range(1,4)] for i in range(1,4)]
[print(val, end="\n") for val in empty_board]

print ("LET'S SEPERATE THESE! " * 3)

#BOARD WITH XOX SHAPE
xox_board = [["X" if val % 2 != 0 else "O" for val in range(1,4)] for i in range(1,4)]
[print(val, end="\n") for val in xox_board]

#NEXT STEP IS BUILDING THE GAME
#I THINK I CAN CODE THE MOVES WITH ACCESSING AND CHANGING THE INDEXES
#BUT ONE MOVE WOULD AFFECT EACH LIST, SO I SHOULD SEPERATE THEM.
#THAT'S A NEW TINY CHALLENGE TO HANDLE <3
