#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 07/22/2013
# Notes:       *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from copy import copy

#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print ('\nINVALID\n')

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


#creates a new logical_expression based on the inputted string
def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print('\nUnexpected end of input.\n')
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):

    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# End of ported code
#-------------------------------------------------------------------------------

#extracts the list of all unique symbols appearing in a statement
def extract_symbols(statement):
    symbols=set()
    if statement.symbol[0]:
        symbols.add(statement.symbol[0])
        return symbols
    for exp in statement.subexpressions:
        symbols=symbols | extract_symbols(exp)
    return symbols


#Student functions
def extend_model(model, key, value):

    model[key] = value
    return model

def tt_check_all(knowledge_base, s, symbols, model):

    #TODO: find a different condition
    if not symbols:
        if statement_truth(knowledge_base, model):
            return statement_truth(s, model)
        else:
            return True

    first = symbols[0]
    # Storing the rest of the symbol
    rest = symbols[1:]

    return tt_check_all( knowledge_base, s, rest, extend_model(model, first, True) ) \
           and tt_check_all( knowledge_base, s, rest, extend_model(model, first, False) )

#kb should include both the actual kb and the additional knowledge
def get_model(knowledge_base):
    model={}
    for sub in knowledge_base.subexpressions:
        #finding true values
        if sub.connective[0] == '':
            model[sub.symbol[0]] = True
        #finding false values
        if sub.connective[0].lower() == 'not':

            if sub.subexpressions[0].symbol \
            and sub.subexpressions[0].connective[0] == '':
               model[sub.subexpressions[0].symbol[0]] = False
    return model
def invert_statement(s):
    return '(not '+ s+ ')'
def inference_engine(knowledge_base, statement):
    #symbols = knowledge_base symbols plus statement symbols
    symbols=list(extract_symbols(knowledge_base))


    alpha = read_expression(statement)
    symbols.extend(list(extract_symbols(alpha)))
    model = get_model(knowledge_base)
    model_alpha=get_model(alpha)
    model={**model, **model_alpha}

    if not valid_expression(alpha):
        sys.exit('invalid statement')

    counter = [0]

    # Convert statement into a logical expression and verify it is valid
    not_alpha = read_expression(invert_statement(statement), counter)
    for key in model.keys():
        symbols.remove(key)
        #could do exception handling...
        # try:
        #
        # except Exception:
        #     pass

    alpha_entailment = tt_check_all(knowledge_base, alpha, list(symbols), model)
    not_alpha_entailment = tt_check_all(knowledge_base, not_alpha, list(symbols), model)

    if alpha_entailment and not not_alpha_entailment:
        return 1
    if not alpha_entailment and not_alpha_entailment:
        return 2
    if not alpha_entailment and not not_alpha_entailment:
        return 3
    if alpha_entailment and not_alpha_entailment:
        return 4

def statement_truth(statement, model):
        if statement.symbol[0]:
            return symbol_truth(model, statement.symbol[0])

        if statement.connective[0].lower() == 'not':
            return not statement_truth(statement.subexpressions[0], model)

        if statement.connective[0].lower() == 'and':

            if statement.subexpressions == ['']:
                return True
            for le in statement.subexpressions:
                if not statement_truth(le, model):
                    return False
            return True

        if statement.connective[0].lower() == 'or':
            if statement.subexpressions == ['']:
                return False

            for le in statement.subexpressions:
                if statement_truth(le, model):
                    return True
            return False

        if statement.connective[0].lower() == "xor":
            if statement.subexpressions == ['']:
                return False
            found_true = True
            for idx, subexpression in enumerate(statement.subexpressions):
                if(idx == 0):
                    found_true = statement_truth(subexpression, model)
                    continue;
                # taking the XOR
                found_true = found_true ^ statement_truth(subexpression, model)
            return found_true

        if statement.connective[0].lower() == 'if':
            if statement_truth(statement.subexpressions[0], model) and not statement_truth(statement.subexpressions[1], model):
                return False
            return True

        if statement.connective[0].lower() == 'iff':
            if statement_truth(statement.subexpressions[0], model) and statement_truth(statement.subexpressions[1], model):
                return True
            return False


def symbol_truth(model, symbol):
    return model[symbol]
