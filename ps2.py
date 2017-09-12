###### this is the second .py file ###########

####### write your code here ##########
choices = [] # creating a list


for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True # starting with player 1 turn
winner = False

def printBoard() : # defining a function print Board
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
	choice = int(input(">>"))
    except:
        print("please enter a valid  no")
        continue


 if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
choices[choice - 1] = 'O'
