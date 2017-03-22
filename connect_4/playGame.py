#this is needed to prevent circular dependence
from AI_Player import *

class PlayGame:
    def __init__(self, maxGame):
        self.game=maxGame
        self.ai=AI_Player(self.game.depth)

    def play(self):
        if self.game.mode:
            self.launchInteractive()
        else:
            self.launchOneMove()
    def launchInteractive(self):
        print ("--------initial--------")
        self.game.printGameBoard()
        print ("--------initial--------")

        while True:

            if self.game.isOver():
                self.game.printGameState()
                break

            #computer player
            elif int(self.game.currentTurn)==1:

                self.game.gameBoard=self.ai.getBestMove(self.game.gameBoard)
                self.game.updateGameState()
                self.game.currentTurn=1 if self.game.currentTurn==2 else 2
                self.game.printGameBoardToFile('computer.txt')
            elif int(self.game.currentTurn)==2:
                print ("Enter the column [1-7]: ")
                humanCol=int(input())-1
                while (humanCol <0 or humanCol >7) or self.game.gameBoard[0][humanCol]:
                    print ("Not in bounds. Enter the column [1-7]: ")
                    humanCol=int(input())
                self.game.gameBoard=self.game.playPiece(humanCol).gameBoard
                self.game.updateGameState()
                self.game.currentTurn=1 if self.game.currentTurn==2 else 2
                self.game.printGameBoardToFile('human.txt')


    def launchOneMove(self):
        self.game.updateGameState()
        if self.game.isOver():
            return
        self.game.gameBoard=self.ai.getBestMove(self.game.gameBoard)
        self.game.updateGameState()
        self.game.currentTurn=1 if self.game.currentTurn==2 else 2
        self.game.printGameBoardToFile(self.game.outputFile)
