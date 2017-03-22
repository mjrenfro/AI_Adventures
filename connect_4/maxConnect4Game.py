import sys
from copy import deepcopy as supercopy
import random as random
#columns are numbered left to right with 1-7
#rows are numbered bottom to top with numbers 1-6

#Move is determined by the player specifying which column to drop the piece at
#if the column is already full then the player must try to make a different Move

#The game is over whe all positions are occupied.
#Each player only makes 21 moves.

#The player with the most four-in the row pieces
    #Horizontally
    #Vertically
    #Diagonally

#Wins the game




#Student code
def parseArgs():
    if len (sys.argv) <4:
        sys.exit('Too few arguments')
    args=sys.argv[1:]
    mode= args[0]
    if mode == "interactive":
        args[0]=1
        #binary-ify the next user
        args[2]=1 if args[2]=="computer-next" else 2
        return args
    else:
        args[0]=0
        return args

class maxConnect4Game:
    def __init__(self, config=None, board=None, player=1):
        #this is for the minimax search
        if config==None:
            self.currentTurn=player
            self.gameBoard=board
            self.player1Score=0
            self.player2Score=0
            self.updatePlayersScore()
            #constants

            self.numRows=6
            self.numCols=7
            random.seed()

        else:
            self.outputFile=None
            self.mode, self.inputFile=config[0], config[1]
            if self.mode:
                self.currentTurn=config[2]
            else:
                self.outputFile=config[2]
            self.depth=int(config[3])
            board=self.makeBoard()
            self.gameBoard=board[:len(board)-1]
            self.currentTurn=board[len(board)-1][0]
            self.player1Score=0
            self.player2Score=0
            self.pieceCount=0
            #constants
            self.numRows=6
            self.numCols=7
            random.seed()




    # def printState(self):
    #     print ("Mode: "self.mode)
    #     print ("Input File: "self.inputFile)
    #     print ("Current Turn: "self.currentTurn)
    #     print ("Depth: "self.depth)
    #     print ("Output File: "self.outputFile)

    def makeBoard(self):
        #read in from file and populate a 2d array

        with open (self.inputFile) as textFile:
            lines=[list(map(int, list(line.strip()))) for line in textFile]
            return lines
        return None

    def make_move(self):
        print (self.gameBoard)



    #Count the number of pieces already played
    # def checkPieceCount(self):
    #     print("piece count")
    #     self.pieceCount=sum(1 for row in self.gameBoard for piece in row if piece)

    def checkPieceCount(self):
        self.pieceCount = 0
        for row in self.gameBoard:
            # print ("each row")
            for piece in row:
                if int(piece) != 0:
                    # print ("incrementing count")
                    self.pieceCount+=1


    def printScores(self):
        print ('Computer Score: ',self.player1Score)
        print ('Human Score: ', self.player2Score)

    def updateGameState(self):
        self.currentTurn=1 if self.currentTurn==2 else 2
        self.updatePlayersScore()

        self.printGameBoard()
        self.printScores()



    #Output current game status to console
    def printGameBoard(self):
        print("-----------------")
        for i in range(6):
            print("|", end="")
            for j in range(7):
                print("{0}".format(self.gameBoard[i][j]), end='')
            print ("|")
        print ("-----------------")



    def isOver(self):
        # print ("is over")
        self.checkPieceCount()
        # print ("pieces:" ,self.pieceCount)
        return self.pieceCount ==42

    #Output current game status to file
    def printGameBoardToFile(self, fileName):
        with open(fileName, 'w') as gameFile:
            for row in self.gameBoard:
                gameFile.write(''.join(str(col) for col in row) +"\r\n")
            gameFile.write("%s\r\n" % str(self.currentTurn))

    #Place the current player's piece in the requested column
    def playPiece(self, column):
        cpyBoard=supercopy(self)
        if not cpyBoard.gameBoard[0][column]:
            for i in range(5,-1,-1):
                if not cpyBoard.gameBoard[i][column]:
                    cpyBoard.gameBoard[i][column]=cpyBoard.currentTurn
                    break
        cpyBoard.currentTurn=1 if self.currentTurn==2 else 2
        # cpyBoard.printGameBoard()
        return cpyBoard



    #The AI section. Currently plays randomly.
    def aiPlay(self):
        randColumn=random.randrange(0,7)
        result=self.playPiece(randColumn)
        if not result:
            self.aiPlay()
        else:
            print("\n\nmove %d, column %d\n" % (self.pieceCount, self.currentTurn, randColumn+1))
            if self.currentTurn==1:
                self.currentTurn=2
            elif self.currentTurn==2:
                self.currentTurn=1
    #utility is simply the amount the computer player
    #is winning with the current board configuration
    def utility (self):
        self.updatePlayersScore()
        return self.player1Score-self.player2Score

    #really? this just restarts the count after every play...that's terrible
    def updatePlayersScore(self):

        self.player1Score=self.countScore(1)
        self.player2Score=self.countScore(2)

    def countScore(self, player):
        score=0
        self.numRows=6
        self.numCols=7
        #Horizontal
        for r in range(0, self.numRows):
            for c in range(0, 4):
                if (self.gameBoard[r][c]==player and self.gameBoard[r][c+1]==player and
                self.gameBoard[r][c+2]==player and self.gameBoard[r][c+3]==player):
                    score+=1
        #Vertical
        for r in range(0, 3):
            for c in range(0, self.numCols):
                if(self.gameBoard[r][c]==player and self.gameBoard[r+1][c]==player and
                self.gameBoard[r+2][c]==player and self.gameBoard[r+3][c] ==player):
                    score+=1

        #Diagonally
        for r in range(0,3):
            for c in range(0, 4):
                if range(self.gameBoard[r][c]==player and self.gameBoard[r+1][c+1]==player and
                self.gameBoard[r+2][c+2]==player and self.gameBoard[r+3][c+3]):
                    score+=1

        for r in range(0,3):
            for c in range(0, 4):
                if range(self.gameBoard[r+3][c]==player and self.gameBoard[r+2][c+1]==player and
                self.gameBoard[r+1][c+2]==player and self.gameBoard[r][c+3]==player):
                    score+=1

        return score

    def countAlmostScores(self, player):
        score=0

        #horizontal
        for r in range(0, self.numRows):
            for c in range(0, 4):
                if(self.gameBoard[r][c]==player and self.gameBoard[r][c+1]==player and
                self.gameBoard[r][c+2]==player and self.gameBoard[r][c+3] ==0):
                    score+=.8
        #Vertical
        for r in range(0, 3):
            for c in range(0, self.numCols):
                if(self.gameBoard[r][c]==player and self.gameBoard[r+1][c]==player and
                self.gameBoard[r+2][c]==player and self.gameBoard[r+3][c] == 0):
                    score+=.8

        #diagonally
        for r in range(0,3):
            for c in range(0, 4):
                if(self.gameBoard[r][c]==player and self.gameBoard[r+1][c+1]==player
                and self.gameBoard[r+2][c+2]==player and self.gameBoard[r+3][c+3]==0):
                    score+=.8

        for r in range(0,3):
            for c in range(0, 4):
                if range(self.gameBoard[r+3][c]==player and self.gameBoard[r+2][c+1]==player and
                self.gameBoard[r+1][c+2]==player and self.gameBoard[r][c+3]==0):
                    score+=.8
        return score
    def evaluation(self):
        return self.countScore(1)+self.countAlmostScores(1) -self.countScore(2)+self.countAlmostScores(2)
