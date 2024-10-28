# TIC TAC TOE
import numpy

board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
player_1_symbol = 'X'
player_2_symbol = 'O'

def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol:
        print(symbol,'won')
        return True


def check_cols(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[c][r]==symbol: #row variable and column constant
                count+=1
        if count==3:
            print(symbol,won)
            return True
        
    return False

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if(count==3):
            print(symbol,'Won the game....')
            return True
        
    return False
                

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):           
        row = int(input("Enter the row (1,2,3) : "))
        col = int(input("Enter the column (1,2,3) : "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid input. Please enter again !!")

    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if(turn%2==0):          #0,2,4,6,8 -> X's Turn
            print('X Turn --->')
            print()
            place(player_1_symbol)
            if won(player_1_symbol):
                break
        else:                   #1,3,5,7 -> O's Turn
            print('O Turn --->')
            print()
            place(player_2_symbol)
            if won(player_2_symbol):
                break

    if not(won(player_1_symbol)) and not(won(player_2_symbol)):
            print("Match Draw !!")

    turn = turn + 1

play()