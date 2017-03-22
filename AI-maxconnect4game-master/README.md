Name: Suyog S Swami
Language Used: Python 2.4

How to run the program:

Place all the 3 python files along with the input file in the omega directory.

type the following command to run 'one-move mode':

 python suyogsmaxconnect4.py one-move input3.txt output.txt 5

type the following command to run 'interactive mode':

python suyogsmaxconnect4.py interactive input3.txt computer-next 5

sample input file is provided along with the code.

The Player.py contains the Minimax algorithm alongwith the alpha beta pruning implemented in it.

The suyogsmaxconnect4.py contains the main function has conditions to follow one-move or interactive mode.
If depth is not provided it works for whole 42 level and takes longer time.. hence puting a level depth of 5-6 is a better idea.

The MaxCOnnect4Game.py contains scoring, printing, checking board, evaluation(for depth limited) and utility function for complete level.etc
