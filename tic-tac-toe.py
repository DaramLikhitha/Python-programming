p1 = input("Player1, choose X or O : ")
if p1=="X":
    player1="X"
    player2="O"
else:
    player1="O"
    player2="X"

print(f"Player1 is {player1} and Player2 is {player2}")

board=[" " for i in range(9)]

def print_board():
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def start_game():
    print("Let's Go...")
    print_board()
    playerturn("1")

def playerturn(turn):
    print(f"Player{turn},it's your turn.")
    pos=input("Choose position 1-9 : ")
    while pos not in "123456789":
        pos=input("Invalid position.Choose again (1-9) : ")
    pos=int(pos)
    symbol=player1 if turn=="1" else player2

    if board[pos-1]==" ":
        board[pos-1]=symbol
        print_board()
        if checkWin():
            return
        turn="2" if turn=="1" else "1"
        playerturn(turn)
    else:
        print("Select other position")
        playerturn(turn)

def checkWin():
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]!=" ":
            if board[i]==player1:
                print("Player1 wins")
                return True
            elif board[i]==player2:
                print("Player2 wins")
                return True
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6]!=" ":
            if board[i]==player1:
                print("Player1 wins")
                return True
            elif board[i]==player2:
                print("Player2 wins")
                return True

    if board[0]==board[4]==board[8]!=" ":
        if board[i]==player1:
            print("Player1 wins")
            return True
        elif board[i]==player2:
            print("Player2 wins")
            return True
    if board[2]==board[4]==board[6]!=" ":
        if board[i]==player1:
            print("Player1 wins")
            return True
        elif board[i]==player2:
            print("Player2 wins")
            return True
    if " " not in board:
        print("Tie!!!")
        return True
    
start_game()