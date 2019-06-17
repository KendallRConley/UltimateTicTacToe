import random

class Board():

    def __init__(self):
        self.spots = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.won = False
        self.winPiece = ' '
        self.lastPlace = 4

    def displayBoard(self):
        print(self.spots[0] + " | " + self.spots[1] + " | " + self.spots[2])
        print("----------")
        print(self.spots[3] + " | " + self.spots[4] + " | " + self.spots[5])
        print("----------")
        print(self.spots[6] + " | " + self.spots[7] + " | " + self.spots[8])


    def getWon(self):
        return self.won

    def getWinPiece(self):
        return self.winPiece

    def playerMove(self, PlayerPiece):
        found = False
        while not found:
            print("Make your move(0-8): ")
            move = int(input())
            if move > 8 or move < 0:
                print("ERROR: Invalid choice. Position must be an int between 0 and 8")
            elif self.spots[move] == ' ':
                print("Placing " + PlayerPiece + " at position " + str(move))
                self.spots[move] = PlayerPiece
                found = True
                self.lastPlace = move
            else:
                print("ERROR: Position is already taken!")

    def getLastPlace(self):
        return self.lastPlace

    # Makes smart move for computer, moving where it can win.
    def smartCompMove(self, CompPiece, PlayerPiece):
        score = 0
        move = 0
        copyBoard = self.spots
        # Check if computer can win, do it
        for i in range(9):
            if copyBoard[i] == ' ':  # If space isnt already taken
                copyBoard[i] = CompPiece  # Set it equal to comp piece to test position
                if self.checkWin() == True:  # If move is winning, make it and return
                    self.compMove(CompPiece, i)
                    return move
                copyBoard[i] = PlayerPiece  # Set it equal to player piece to test if losing
                if self.checkWin() == True:  # If losing, take note
                    score = -1
                    move = i
                copyBoard[i] = ' '
        if score == -1:  # Make move to block user
            self.compMove(CompPiece, move)
            self.lastPlace = move
        else:  # If no winning or blocking move is found, pick one at random
            found = False
            while not found:  # Loop until a move is made
                move = random.randint(0, 8)
                if self.spots[move] == ' ':
                    self.compMove(CompPiece, move)
                    found = True
                    self.lastPlace = move

    # Saves the move
    def compMove(self, CompPiece, move):
        print("Computer places piece at position " + str(move))
        self.spots[move] = CompPiece
        self.lastPlace = move

    def checkWin(self):
        return (((self.spots[0] == self.spots[1] == self.spots[2]) and (self.spots[0] != ' ')) or
                ((self.spots[3] == self.spots[4] == self.spots[5]) and (self.spots[3] != ' ')) or
                ((self.spots[6] == self.spots[7] == self.spots[8]) and (self.spots[6] != ' ')) or
                ((self.spots[0] == self.spots[3] == self.spots[6]) and (self.spots[0] != ' ')) or
                ((self.spots[1] == self.spots[4] == self.spots[7]) and (self.spots[1] != ' ')) or
                ((self.spots[2] == self.spots[5] == self.spots[8]) and (self.spots[2] != ' ')) or
                ((self.spots[0] == self.spots[4] == self.spots[8]) and (self.spots[0] != ' ')) or
                ((self.spots[2] == self.spots[4] == self.spots[6]) and (self.spots[2] != ' ')))

    def checkFull(self):
        for i in range(9):
            if (self.spots[i] == ' '):
                return False
        return True