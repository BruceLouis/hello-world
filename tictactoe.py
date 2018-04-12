import random
import os

def clear():
    os.system( 'cls' )
    
def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        print 'Player 1 goes first'
    else:
        print 'Player 2 goes first'
        
    return flip 

def display_board(board):
    print '---------'
    for row in board:
        print str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2])
        print '---------'

def player_input1():
    player = input('Enter key for player 1:')
    while check_for_space(board, player) != True:
        player = input('Enter key for player 1:')        
    place_marker(board, player,'x')

def player_input2():
    player = input('Enter key for player 2:')
    while check_for_space(board, player) != True:
        player = input('Enter key for player 2:')
    place_marker(board, player,'o')
    
def place_marker(board, marker_input, player_input):
    for row in board:
        for column, element in enumerate(row):
            if marker_input == element:              
                row[column] = player_input 
                
def check_for_win(board):
    winner = False

#check for horizontal win
    for row in board:
        if len(set(row)) <= 1:
            winner = True
            
#check for vertical win
    vert_board = zip(*board)
    for column in vert_board:
        if len(set(column)) <= 1:
            winner = True

#check for diagonal win
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        winner = True
    if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        winner = True
    if board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        winner = True
    if board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        winner = True
    
    return winner

def check_full_board(board):
    full_board = False
    count = 0
    for row in board:
        if 'x' in set(row) and 'o' in set(row) and len(set(row)) <= 2:
            count += 1
          
    if count >= 3:
        full_board = True
    
    return full_board
        
    
def check_for_space(board, mark):
    for row in board:
        if mark in row:
            return True
    else:
        print 'space taken'
        return False
    
def board_state(board):    
    if check_for_win(board) == True:
        print 'we have a winner'
        return True
    elif check_full_board(board) == True:
        print 'board is full'
        return True
    else:
        return False

while True:
    board = [[1,2,3],[4,5,6],[7,8,9]]  
    clear()
    display_board(board)
    the_flip = coin_flip()
    while check_for_win(board) != True and check_full_board(board) != True:
        if the_flip == 0:
            player_input1()
            clear()
            display_board(board)
            if board_state(board):
                break
            player_input2()
        else:
            player_input2()
            clear()
            display_board(board)
            if board_state(board):
                break
            player_input1()
        clear()         
        display_board(board)
        if board_state(board):
            break
    
    replay = input('press 1 for replay: ')
    if replay != 1:
        break