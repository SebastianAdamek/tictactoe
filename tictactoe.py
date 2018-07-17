# -*- coding: UTF-8 -*-

import copy

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

theWinnerStage = {'top-L': [('top-M', 'top-R'), ('mid-L', 'low-L'), ('mid-M', 'low-R')],
                  'top-M': [('top-L', 'top-R'), ('mid-M', 'low-M')],
                  'top-R': [('top-M', 'top-L'), ('mid-R', 'low-R'), ('mid-M', 'low-L')],
                  'mid-L': [('top-L', 'low-L'), ('mid-M', 'mid-R')],
                  'mid-M': [('top-L', 'low-R'), ('mid-L', 'mid-R'), ('low-L', 'top-R'), ('top-M', 'low-M')],
                  'mid-R': [('top-R', 'low-R'), ('mid-M', 'mid-L')],
                  'low-L': [('top-L', 'mid-L'), ('mid-M', 'top-R'), ('low-M', 'low-R')],
                  'low-M': [('low-L', 'low-R'), ('mid-M', 'top-M')],
                  'low-R': [('low-M', 'top-L'), ('mid-M', 'top-L'), ('mid-R', 'top-R')]}

def printBoard(board):
    print(" {} | {} | {} ".format(board['top-L'], board['top-M'], board['top-R']))
    print("---+---+---")
    print(" {} | {} | {} ".format(board['mid-L'], board['mid-M'], board['mid-R']))
    print("---+---+---")
    print(" {} | {} | {} ".format(board['low-L'], board['low-M'], board['low-R']))


def printBoardA(theBoard):
    print()
    for i, val in enumerate(theBoard):
        if (i + 1) % 3 == 0 and i != 0:
            print(' {} '.format(theBoard[val]), end='')
            if (i + 1) != 9:
                print("\n---+---+---")
            continue
        print(" {} |".format(theBoard[val]), end='')
    print()


turn = 'X'
bor = copy.copy(theBoard)
i = 0

while i < 9:
    printBoardA(bor)
    print('Turn for ' + turn + '. Move on witch space?')
    move = input()
    if move in bor and bor[move] == ' ':
        bor[move] = turn
        i += 1
        for win in theWinnerStage[move]:
            print('')
            if bor[win[0]] == turn and bor[win[1]] == turn:
                print("Gamer  - {} - is the winner".format(turn).upper())
                printBoard(bor)
                exit()
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    elif move == 'clear':
        bor = copy.copy(theBoard)
        turn = 'X'
        continue
    elif move == 'exit':
        print('Thank you for game'.upper())
        break
        # exit()
    elif move in bor and bor[move] != ' ':
        print("This area is restricted! Please try again".upper())
        continue
    else:
        print('I don\'t understand this command!'.upper())
printBoardA(bor)

