print("welcome to TicTactToe")
# cells of the TicTacToe game
Cells = ['o', '1', '2', '3', '4', '5', '6', '7', '8', '9']

player = 1


# Prints the grid of TicTacToe as the game progresses
def PrintGrid():
    print("Player 1: X  vs  Player 2: O")
    print("     |     |     ")
    print("  " + Cells[1] + "  |  " + Cells[2] + "  |  " + Cells[3] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + Cells[4] + "  |  " + Cells[5] + "  |  " + Cells[6] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + Cells[7] + "  |  " + Cells[8] + "  |  " + Cells[9] + "  ")
    print("     |     |     ")


# winning conditions
def hasWon():
    if Cells[1] == Cells[2] == Cells[3]:
        return True
    elif Cells[4] == Cells[5] == Cells[6]:
        return True
    elif Cells[7] == Cells[8] == Cells[9]:
        return True
    elif Cells[4] == Cells[5] == Cells[6]:
        return True
    elif Cells[1] == Cells[5] == Cells[9]:
        return True
    elif Cells[3] == Cells[5] == Cells[7]:
        return True
    elif (Cells[1] != '1' and Cells[2] != '2' and Cells[3] != '3' and Cells[4] != '4' and Cells[5] != '5'
          and Cells[6] != '6' and Cells[7] != '7' and Cells[8] != '8' and Cells[9] != '9'):
        return False
    else:
        return -1

# Main
# Beginning of the main Function


player = player % 2
check = -1

# only ends when check changes which is returned by the hasWon function
while check == -1:
    PrintGrid()
    if player % 2:
        player = 1
    else:
        player = 2
    print("player ", end="")
    print(player, end="")
    play = int(input(" enter a number"))

    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    print("player " + str(player) + " Played in the cell number " + str(play))

    if play == 1 and Cells[1] == '1':
        Cells[1] = mark
    if play == 2 and Cells[2] == '2':
        Cells[2] = mark
    if play == 3 and Cells[3] == '3':
        Cells[3] = mark
    if play == 4 and Cells[4] == '4':
        Cells[4] = mark
    if play == 5 and Cells[5] == '5':
        Cells[5] = mark
    if play == 6 and Cells[6] == '6':
        Cells[6] = mark
    if play == 7 and Cells[7] == '7':
        Cells[7] = mark
    if play == 8 and Cells[8] == '8':
        Cells[8] = mark
    if play == 9 and Cells[9] == '9':
        Cells[9] = mark
    else:
        print("invalid input skipping your turn")

    player = player + 1
    check = hasWon()

PrintGrid()
# winner winner
if check == 1:
    print("Player ", end="")
    print(player - 1, end="")
    print(" won!", end="")
else:  # Otherwise, it's a tie
    print("It's a tie no one has won")
