from random import randint
def show_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")

def checkForWin(player):
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    else:
        return False

def player1():
    position = int(input("Which position for player x?"))
    if board[position] == ' ':
        board[position] = "x"
    else:
        print("This position has already been taken.\n")
        player1()
    show_board()
    if checkForWin("x"):
        print("x is the winner.")
        return True
    
def minmax(board,is_maximizing):
    if checkForWin('o'):
        return 1
    elif checkForWin('x'):
        return -1
    elif checkForDraw():
        return 0
    
    if is_maximizing:
        best_score = -100
        best_move = 0
        for key in board.keys():
            if board[key]==' ':
                board[key] = 'o'
                score = minmax(board,False)
                board[key]=' '
                if score > best_score:
                    best_score = score
                    
        return best_score
    
    else:
        best_score = 100
        best_move = 0
        for key in board.keys():
            if board[key]==' ':
                board[key] = 'x'
                score = minmax(board,True)
                board[key]=' '
                if score < best_score:
                    best_score = score
                    
        return best_score
        



def player2():
    best_score = -100
    best_move = 0
    for key in board.keys():
        if board[key]==' ':
            board[key] = 'o'
            score = minmax(board,False)
            board[key]=' '
            if score > best_score:
                best_score = score
                best_move = key
        position = best_move
    if board[position] == ' ':
        board[position] = "o"
    else:
        print("This position has already been taken.\n")
        player2()
    show_board()
    if checkForWin("o"):
        print("o is the winner.")
        return True
    
def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True




board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

show_board()


while True:
    if player1():break
    if player2():break
        
   
    



   

