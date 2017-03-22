#Simply the runner function

from maxConnect4Game import *
from playGame import *

if __name__ =='__main__':
    args=parseArgs()
    game=maxConnect4Game(args)
    playG = PlayGame(game)
    playG.play()

    # attrs=vars(game)
    # print (', '.join("%s: %s" % item for item in attrs.items()))
