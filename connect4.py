

imaginary_Field= [[" ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " "]]

def Drawfield(field):
    for row in range(12):  # 0,1,2,3,4,5,6,7,8,9,10,11
        if row % 2 == 0:
            pracRow=int(row/2)  # 0,-,1,-,2,-,3,-,4,-,5,-
            for column in range(13):  # 0,1,2,3,4,5,6,7,8,9,10,11,12,13
                if column % 2 == 0:
                    print(" | ", end="")
                else:
                    pracColumn = int(column / 2) # 0,-,1,-,2,-,3,-,4,-, 5,- ,6
                    print(field[pracRow][pracColumn], end="")
        else:
            print()
            print("-" * 27)

def ActualBoard():
    print("  column=       0   1   2   3   4   5")
    print("  row:0       |   |   |   |   |   |   |")
    print("             ---------------------------")
    print("  row:1       |   |   |   |   |   |   |")
    print("             ---------------------------")
    print("  row:2       |   |   |   |   |   |   |")
    print("             ---------------------------")
    print("  row:3       |   |   |   |   |   |   |")
    print("             ---------------------------")
    print("  row:4       |   |   |   |   |   |   |")
    print("             ---------------------------")
    print("  row:5       |   |   |   |   |   |   |")
    print("             ---------------------------")
print("Welcome to Connect4\n")
PlayerOneChoice= input("Enter a sign player 1 would love to see: ")
PlayerTwoChoice= input("Enter a sign player 2 would love to see: ")

def PlayerTurn():
    player=1
    while (True):
        print("player's turn: ", player)
        # if there is no exception
        try:
            Row_Turn = int(input("Enter a row: "))
            Turn_Column = int(input("Enter a column: "))
            if player == 1:
                if imaginary_Field[Row_Turn][Turn_Column] == " ":
                    imaginary_Field[Row_Turn][Turn_Column] = PlayerOneChoice
                    if imaginary_Field[0][0] == PlayerOneChoice and imaginary_Field[0][1] == PlayerOneChoice and imaginary_Field[0][2] == PlayerOneChoice and imaginary_Field[0][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][1] == PlayerOneChoice and imaginary_Field[0][2] == PlayerOneChoice and imaginary_Field[0][3] == PlayerOneChoice and imaginary_Field[0][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][2] == PlayerOneChoice and imaginary_Field[0][3] == PlayerOneChoice and imaginary_Field[0][4] == PlayerOneChoice and imaginary_Field[0][5] == PlayerOneChoice:

                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][0] == PlayerOneChoice and imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[1][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[1][4] == PlayerOneChoice and imaginary_Field[1][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][0] == PlayerOneChoice and imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[2][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[3][0] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice and imaginary_Field[3][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[4][0] == PlayerOneChoice and imaginary_Field[4][1] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[4][1] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice and imaginary_Field[4][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[5][0] == PlayerOneChoice and imaginary_Field[5][1] == PlayerOneChoice and imaginary_Field[5][2] == PlayerOneChoice and imaginary_Field[5][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[5][1] == PlayerOneChoice and imaginary_Field[5][2] == PlayerOneChoice and imaginary_Field[5][3] == PlayerOneChoice and imaginary_Field[5][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[5][2] == PlayerOneChoice and imaginary_Field[5][3] == PlayerOneChoice and imaginary_Field[5][4] == PlayerOneChoice and imaginary_Field[5][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][0] == PlayerOneChoice and imaginary_Field[1][0] == PlayerOneChoice and imaginary_Field[2][0] == PlayerOneChoice and imaginary_Field[3][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][0] == PlayerOneChoice and imaginary_Field[2][0] == PlayerOneChoice and imaginary_Field[3][0] == PlayerOneChoice and imaginary_Field[4][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][0] == PlayerOneChoice and imaginary_Field[3][0] == PlayerOneChoice and imaginary_Field[4][0] == PlayerOneChoice and imaginary_Field[5][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][1] == PlayerOneChoice and imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[4][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[4][1] == PlayerOneChoice and imaginary_Field[5][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][2] == PlayerOneChoice and imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[5][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][3] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice and imaginary_Field[5][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][4] == PlayerOneChoice and imaginary_Field[1][4] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][4] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice and imaginary_Field[5][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][5] == PlayerOneChoice and imaginary_Field[1][5] == PlayerOneChoice and imaginary_Field[2][5] == PlayerOneChoice and imaginary_Field[3][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][5] == PlayerOneChoice and imaginary_Field[2][5] == PlayerOneChoice and imaginary_Field[3][5] == PlayerOneChoice and imaginary_Field[4][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][5] == PlayerOneChoice and imaginary_Field[3][5] == PlayerOneChoice and imaginary_Field[4][5] == PlayerOneChoice and imaginary_Field[5][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][0] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[5][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][0] == PlayerOneChoice and imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice and imaginary_Field[5][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][0] == PlayerOneChoice and imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][1] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][4] == PlayerOneChoice and imaginary_Field[5][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][1] == PlayerOneChoice and imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice and imaginary_Field[4][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][2] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][5] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][3] == PlayerOneChoice and imaginary_Field[1][2] == PlayerOneChoice and imaginary_Field[2][1] == PlayerOneChoice and imaginary_Field[3][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][4] == PlayerOneChoice and imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][3] == PlayerOneChoice and imaginary_Field[2][2] == PlayerOneChoice and imaginary_Field[3][1] == PlayerOneChoice and imaginary_Field[4][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[0][5] == PlayerOneChoice and imaginary_Field[1][4] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][4] == PlayerOneChoice and imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][3] == PlayerOneChoice and imaginary_Field[3][2] == PlayerOneChoice and imaginary_Field[4][1] == PlayerOneChoice and imaginary_Field[5][0] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[1][5] == PlayerOneChoice and imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][4] == PlayerOneChoice and imaginary_Field[3][3] == PlayerOneChoice and imaginary_Field[4][2] == PlayerOneChoice and imaginary_Field[5][1] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    elif imaginary_Field[2][5] == PlayerOneChoice and imaginary_Field[3][4] == PlayerOneChoice and imaginary_Field[4][3] == PlayerOneChoice and imaginary_Field[5][2] == PlayerOneChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 1 Wins")
                        break
                    player = 2
            else:
                if imaginary_Field[Row_Turn][Turn_Column] == " ":
                    imaginary_Field[Row_Turn][Turn_Column] = PlayerTwoChoice
                    if imaginary_Field[0][0] == PlayerTwoChoice and imaginary_Field[0][1] == PlayerTwoChoice and imaginary_Field[0][2] == PlayerTwoChoice and imaginary_Field[0][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][1] == PlayerTwoChoice and imaginary_Field[0][2] == PlayerTwoChoice and imaginary_Field[0][3] == PlayerTwoChoice and imaginary_Field[0][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][2] == PlayerTwoChoice and imaginary_Field[0][3] == PlayerTwoChoice and imaginary_Field[0][4] == PlayerTwoChoice and imaginary_Field[0][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][0] == PlayerTwoChoice and imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[1][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[1][4] == PlayerTwoChoice and imaginary_Field[1][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][0] == PlayerTwoChoice and imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[2][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[3][0] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice and imaginary_Field[3][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[4][0] == PlayerTwoChoice and imaginary_Field[4][1] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[4][1] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice and imaginary_Field[4][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice and imaginary_Field[4][4] == PlayerTwoChoice and imaginary_Field[4][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[5][0] == PlayerTwoChoice and imaginary_Field[5][1] == PlayerTwoChoice and imaginary_Field[5][2] == PlayerTwoChoice and imaginary_Field[5][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[5][1] == PlayerTwoChoice and imaginary_Field[5][2] == PlayerTwoChoice and imaginary_Field[5][3] == PlayerTwoChoice and imaginary_Field[5][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[5][2] == PlayerTwoChoice and imaginary_Field[5][3] == PlayerTwoChoice and imaginary_Field[5][4] == PlayerTwoChoice and imaginary_Field[5][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][0] == PlayerTwoChoice and imaginary_Field[1][0] == PlayerTwoChoice and imaginary_Field[2][0] == PlayerTwoChoice and imaginary_Field[3][0] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][0] == PlayerTwoChoice and imaginary_Field[2][0] == PlayerTwoChoice and imaginary_Field[3][0] == PlayerTwoChoice and imaginary_Field[4][0] == PlayerTwoChoice:
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][0] == PlayerTwoChoice and imaginary_Field[3][0] == PlayerTwoChoice and imaginary_Field[4][0] == PlayerTwoChoice and imaginary_Field[5][0] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][1] == PlayerTwoChoice and imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[4][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[4][1] == PlayerTwoChoice and imaginary_Field[5][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][2] == PlayerTwoChoice and imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[5][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][3] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice and imaginary_Field[5][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][4] == PlayerTwoChoice and imaginary_Field[1][4] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][4] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][4] ==  PlayerTwoChoice and imaginary_Field[4][4] ==  PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice and imaginary_Field[4][4] == PlayerTwoChoice and imaginary_Field[5][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][5] == PlayerTwoChoice and imaginary_Field[1][5] == PlayerTwoChoice and imaginary_Field[2][5] == PlayerTwoChoice and imaginary_Field[3][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][5] == PlayerTwoChoice and imaginary_Field[2][5] == PlayerTwoChoice and imaginary_Field[3][5] == PlayerTwoChoice and imaginary_Field[4][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][5] == PlayerTwoChoice and imaginary_Field[3][5] == PlayerTwoChoice and imaginary_Field[4][5] == PlayerTwoChoice and imaginary_Field[5][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][0] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[5][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][0] == PlayerTwoChoice and imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice and imaginary_Field[5][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][0] == PlayerTwoChoice and imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][1] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][4] == PlayerTwoChoice and imaginary_Field[5][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][1] == PlayerTwoChoice and imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice and imaginary_Field[4][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][2] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][5] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][3] == PlayerTwoChoice and imaginary_Field[1][2] == PlayerTwoChoice and imaginary_Field[2][1] == PlayerTwoChoice and imaginary_Field[3][0] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][4] == PlayerTwoChoice and imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][3] == PlayerTwoChoice and imaginary_Field[2][2] == PlayerTwoChoice and imaginary_Field[3][1] == PlayerTwoChoice and imaginary_Field[4][0] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[0][5] == PlayerTwoChoice and imaginary_Field[1][4] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][4] == PlayerTwoChoice and imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][3] == PlayerTwoChoice and imaginary_Field[3][2] == PlayerTwoChoice and imaginary_Field[4][1] == PlayerTwoChoice and imaginary_Field[5][0] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[1][5] == PlayerTwoChoice and imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][4] == PlayerTwoChoice and imaginary_Field[3][3] == PlayerTwoChoice and imaginary_Field[4][2] == PlayerTwoChoice and imaginary_Field[5][1] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    elif imaginary_Field[2][5] == PlayerTwoChoice and imaginary_Field[3][4] == PlayerTwoChoice and imaginary_Field[4][3] == PlayerTwoChoice and imaginary_Field[5][2] == PlayerTwoChoice:
                        Drawfield(field=imaginary_Field)
                        print("Player 2 Wins!")
                        break
                    player = 1
            Drawfield(field=imaginary_Field)
        # exception handled
        except ValueError as e:
            print("Warning!! Please enter a valid value. ",e)
        except IndexError as e:
            print("Warning!! your entry is out of index range.\nPlease check the board again. ",e,ActualBoard())
        finally:
            PlayerTurn()

need_help=input("For Help press H or simply proceed: ")
if need_help== "H":
    InstructionForPlayers= input("This game board is designed according to python list index.\nTo see the pattern of the board type yes/no: ")
    if InstructionForPlayers=="yes":
        ActualBoard()
        PlayerTurn()
    else:
        PlayerTurn()
PlayerTurn()

