###############################################################################
##  Name - Suyog S Swami
##  Subject: CSE5360 Artificial Intelligence 1
##  Assignement: MaxConnect4 game using Minimax and alpha beta pruning
##  Students ID: 1001119101
###############################################################################

import Player as p
import sys

def main(argv):
    nextPlayer = ''
    inputFile = ''
    outputFile = ''
    gameMode = argv[1]

    if gameMode == 'interactive':
        inputFile = argv[2]
        nextPlayer = argv[3]
        initnextplayer=nextPlayer
        player = p.Player()
        player.depth_limit = int(argv[4])
        initstate = player.setInitState(inputFile,gameMode,nextPlayer)
        while True:
            count = initstate.checkPieceCount()
            if count == 42 and initnextplayer=='computer-next':
                initstate.countScore()
                print 'Computers Score: ', initstate.player1score
                print 'Players core:', initstate.player2score
                initstate.printGameBoard()
                break
            elif count==42 and initnextplayer=='human-next':
                initstate.countScore()
                print 'Computers Score: ', initstate.player2score
                print 'Players core:', initstate.player1score
                initstate.printGameBoard()
                break

            elif nextPlayer == 'computer-next':
                initstate, move, score = player.minimaxDecision(initstate)
                initstate.countScore()
                print 'Computer Score: ', initstate.player1score
                print 'Players scores:', initstate.player2score
                initstate.printBoardToFile('computer.txt')
                nextPlayer = 'human-next'

            elif nextPlayer == 'human-next':
                initstate.countScore()
                initstate.printGameBoard()
                print 'Computer Score:', initstate.player2score
                print 'Players Score: ', initstate.player1score
                print "Enter column between 1-7:"
                humanMove = int(raw_input())
                while humanMove<1 or humanMove>7:
                    print "Enter column between 1-7:"
                    humanMove = int(raw_input())
                isValid, initstate = initstate.playPiece(humanMove-1)
                while not isValid:
                    print "Enter column between 1-7:"
                    humanMove = int(raw_input())
                    isValid, initstate = initstate.playPiece(humanMove-1)
                initstate.printBoardToFile('human.txt')
                nextPlayer = 'computer-next'

    elif gameMode == 'one-move':
        inputFile = argv[2]
        outputFile = argv[3]
        player = p.Player()
        player.depth_limit = int(argv[4])
        initstate = player.setInitState(inputFile,gameMode,nextPlayer)
        temp, move, score = player.minimaxDecision(initstate)
        print 'Move : Column', move+1
        print 'Score:', score
        print 'GameBoard after column',move+1,'move:'
        temp.printGameBoard()
        temp.printBoardToFile(outputFile)

if __name__ == '__main__':
    main(sys.argv)