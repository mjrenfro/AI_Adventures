#!/usr/bin/env python

#Takes in an text file called "result.txt"
#Uses the truth table inference approach to determine truth or falseness of statement
#There four possible values for output
    #Definitely true
        #KB entails the statement
        #KB does not entail the negation
    #Definitely false
        #KB entails the negation of the statement
        #KB does not entail the statement
    #Possibly true, possibly false
        #KB entails neither the statement nor the negation of the statement
    #both true and false
        #means something is wrong with the KB
        #KB entails both the statement and the negation of the statement
import sys
from logical_expression import *
def interpret_result(x):
    return {
        1 : 'Definitely True',
        2: 'Definitely False',
        3: 'Possibly True, Possibly False',
        4: 'Both True and False',

    }[x]

def check_true_false(knowledge_base, statement):
    return(interpret_result(inference_engine(knowledge_base, statement)))

def main(argv):
    if len(argv) != 4:
        print('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0])
        sys.exit(0)

    # Read wumpus rules file
    try:
        input_file = open(argv[1], 'r')
    except:
        print('failed to open file %s' % argv[1])
        sys.exit(0)

    # Create the knowledge base with wumpus rules
    print ('\nLoading wumpus rules...')
    knowledge_base = logical_expression()
    knowledge_base.connective = ['and']
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # A mutable counter so recursive calls don't just make a copy
        subexpression = read_expression(line.rstrip('\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Read additional knowledge base information file
    try:
        input_file = open(argv[2], 'r')
    except:
        print('failed to open file %s' % argv[2])
        sys.exit(0)

    # Add expressions to knowledge base
    print ('Loading additional knowledge...')
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # a mutable counter
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Verify it is a valid logical expression
    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    # I had left this line out of the original code. If things break, comment out.
    # print_expression(knowledgebase, '\n')

    # Read statement whose entailment we want to determine
    try:
        input_file = open(argv[3], 'r')
    except:
        print('failed to open file %s' % argv[3])
        sys.exit(0)
    print ('Loading statement...')
    statement = input_file.readline().rstrip('\r\n')
    input_file.close()

    # Run the statement through the inference engine
    result =check_true_false(knowledge_base, statement)
    print ("Result: ", result , "\n")

    try:
        output_file=open('result.txt', 'w')
    except:
        print('failed opening the output file')

    output_file.write(result)
    output_file.close()

    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
