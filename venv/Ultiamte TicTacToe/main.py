from board import Board
import random


def displayBoards(boards):
    for i in range(9):
        print("Board: " + str(i))
        boards[i].displayBoard()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def checkBigWin(boards):
    return (((boards[0].winPiece == boards[1].winPiece == boards[2].winPiece) and (boards[0].winPiece != ' ')) or
            ((boards[3].winPiece == boards[4].winPiece == boards[5].winPiece) and (boards[3].winPiece != ' ')) or
            ((boards[6].winPiece == boards[7].winPiece == boards[8].winPiece) and (boards[6].winPiece != ' ')) or
            ((boards[0].winPiece == boards[3].winPiece == boards[6].winPiece) and (boards[0].winPiece != ' ')) or
            ((boards[1].winPiece == boards[4].winPiece == boards[7].winPiece) and (boards[1].winPiece != ' ')) or
            ((boards[2].winPiece == boards[5].winPiece == boards[8].winPiece) and (boards[2].winPiece != ' ')) or
            ((boards[0].winPiece == boards[4].winPiece == boards[8].winPiece) and (boards[0].winPiece != ' ')) or
            ((boards[2].winPiece == boards[4].winPiece == boards[6].winPiece) and (boards[2].winPiece != ' ')))

def checkBigFull(boards):
    for i in range(9):
        if (boards[i].winPiece == ' '):
            return False
    print("Its a tie!")
    return True

game = True
while game:
    boards = []
    for integer in range(9):
        board = Board()
        boards.append(board)

    #Handles who goes when
    print("Do you want to go first(X) or second(O)?")
    inp = False
    while not inp:
        if (input() == 'X'):
            Player = 'X'
            Comp = 'O'
            inp = True
        elif input() == 'O':
            Player = 'O'
            Comp = 'X'
            inp = True
        else:
            print("ERROR: enter valid input! O or X only.")

    displayBoards(boards)
    inGame = True
    currentBoard = 4
    while inGame:
        if (Player == 'X'):
            while boards[currentBoard].checkFull == True or boards[currentBoard].won!= False:
                print("Pick board")
                currentBoard = int(input())
            print("current board: " +  str(currentBoard))
            boards[currentBoard].playerMove(Player)
            if(boards[currentBoard].checkWin()):
                boards[currentBoard].won = True
                boards[currentBoard].winPiece = Player
                print("Player has won board " + str(currentBoard))
            if(checkBigWin(boards)):
                print("You win!")
                inGame = False
                break
            if (checkBigFull(boards)):
                inGame = False
                break
            displayBoards(boards)
            if (boards[currentBoard].checkFull == False or boards[currentBoard].won == False):
                currentBoard = boards[currentBoard].getLastPlace()
            while boards[currentBoard].checkFull == True or boards[currentBoard].won == True:
                print("Board " +  str(currentBoard) + " is full.")
                currentBoard = random.randint(0, 8)
                print("Board " + str(currentBoard) + " is the new board.")
            boards[currentBoard].smartCompMove(Comp, Player)
            if (boards[currentBoard].checkWin()):
                boards[currentBoard].won = True
                boards[currentBoard].winPiece = Comp
                print("Computer has won board " + str(currentBoard))
            if (checkBigWin(boards)):
                print("You have lost!")
                inGame = False
                break
            if (checkBigFull(boards)):
                inGame = False
                break
            if (boards[currentBoard].checkFull == False or boards[currentBoard].won == False):
                currentBoard = boards[currentBoard].getLastPlace()
            displayBoards(boards)

        else:
            if (boards[currentBoard].checkFull == False or boards[currentBoard].won == False):
                currentBoard = boards[currentBoard].getLastPlace()
            while boards[currentBoard].checkFull == True or boards[currentBoard].won != False:
                print("Board " + str(currentBoard) + " is full.")
                currentBoard = random.randint(0, 8)
                print("Board " + str(currentBoard) + " is the new board.")
            boards[currentBoard].smartCompMove(Comp, Player)
            if (boards[currentBoard].checkWin()):
                boards[currentBoard].won = True
                boards[currentBoard].winPiece = Comp
                print("Computer has won board " + str(currentBoard))
            if (checkBigWin(boards)):
                print("You have lost!")
                inGame = False
                break
            if (checkBigFull(boards)):
                inGame = False
                break
            displayBoards(boards)
            if (boards[currentBoard].checkFull == False or boards[currentBoard].won == False):
                currentBoard = boards[currentBoard].getLastPlace()
            while boards[currentBoard].checkFull == True or boards[currentBoard].won != False:
                print("Pick board")
                currentBoard = int(input())
            print("current board: " + str(currentBoard))
            boards[currentBoard].playerMove(Player)
            if (boards[currentBoard].checkWin()):
                boards[currentBoard].won = True
                boards[currentBoard].winPiece = Player
                print("Player has won board " + str(currentBoard))
            if (checkBigWin(boards)):
                print("You win!")
                inGame = False
                break
            if (checkBigFull(boards)):
                inGame = False
                break
            displayBoards(boards)

    print("Do you want to continue (N or n to exit)?")
    if (input() == 'N' or input() == 'n'):
        game = False
