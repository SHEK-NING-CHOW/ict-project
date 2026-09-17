# _ for available space
# X for hit ship
# O for ship
# / for miss

import random

player_board=[['_']*10 for _ in range(10)]
bot_board=[['_']*10 for _ in range(10)]
guess_board=[['_']*10 for _ in range(10)]

def print_board(board):
    print("  0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(board[i][j], end=' ')
        print()

def place_ship(board):
    fleet={"Carrier":5, "Battleship":4, "Cruiser":3, "Submarine":3, "Destroyer":2}
    placed_ships=[]
    while len(fleet)>0:
        ship=input("Enter the name of the ship you want to place "
        "(Carrier(5), Battleship(4), Cruiser(3), Submarine(3), Destroyer(2)): ")

        if ship not in fleet:
                print("ship is placed already or invalid ship name")
        else:
                str_row=int(input("Enter the starting row number (0-9) for the ship: "))
                str_col=int(input("Enter the starting column number (0-9) for the ship: "))
                orientation=input("Enter the orientation of the ship (H for horizontal, V for vertical): ")
                size=fleet[ship]
                if str_row<0 or str_row>9 or str_col<0 or str_col>9:
                    print("stop playing")
                    continue
                if orientation=="H":
                    end_row=str_row
                    end_col=str_col+size-1
                elif orientation=="V":
                    end_row=str_row+size-1
                    end_col=str_col
                else:
                    print("stop playing")
                    continue
                if end_row>9 or end_col>9:
                    print("ship is out of bounds, try again")
                    continue
                overlap=False
                for r in range(str_row, end_row+1):
                    for c in range(str_col, end_col+1):
                        if board[r][c]=='O':
                            overlap=True
                if overlap==True:
                    print("overlapped with another ship, try again")
                    continue
                else:
                    if orientation=="H":
                        for i in range(size):
                            board[str_row][str_col+i]='O'
                    elif orientation=="V":
                        for i in range(size):
                            board[str_row+i][str_col]='O'
                    placed_ships.append(ship)
                    fleet.pop(ship)
                    print_board(board)

def bot_ship(board):
    fleet={"Carrier":5, "Battleship":4, "Cruiser":3, "Submarine":3, "Destroyer":2}
    placed_ships=[]
    while len(fleet)>0:
        ship=random.choice(list(fleet.keys()))
        str_row=random.randint(0,9)
        str_col=random.randint(0,9)
        orientation=random.choice(["H","V"])
        size=fleet[ship]
        if orientation=="H":
            end_row=str_row
            end_col=str_col+size-1
        elif orientation=="V":
            end_row=str_row+size-1
            end_col=str_col
        if(end_row>9 or end_col>9):
            continue
        overlap=False
        for r in range(str_row, end_row+1):
            for c in range(str_col, end_col+1):
                if board[r][c]=='O':
                    overlap=True
        if overlap==True:
            continue
        else:
            for r in range(str_row, end_row+1):
                for c in range(str_col, end_col+1):
                    board[r][c]='O'
            placed_ships.append(ship)
            fleet.pop(ship)

def player_turn():
    in_turn=True
    while in_turn is True:
        r=int(input("Enter the row number that you want to attack:"))
        c=int(input("Enter the column number that you want to attack:"))
        if r<0 or r>9 or c<0 or c>9:
            print("Stop playing")
            continue
        elif guess_board[r][c]=='X' or guess_board[r][c]=='/':
            print("You have attacked this position already")
            continue
        elif bot_board[r][c]=='O':
            guess_board[r][c]='X'
            bot_board[r][c]='X'
            print("You hit the bot's ship")
            print_board(guess_board)
            check_winner()
        else:
            guess_board[r][c]='/'
            print("You missed")
            print_board(guess_board)
            in_turn=False

def bot_turn():
    bot_in_turn=True
    while bot_in_turn is True:
        r=random.randint(0,9)
        c=random.randint(0,9)
        if player_board[r][c]=='X' or player_board[r][c]=='/':
            continue
        elif player_board[r][c]=='O':
            player_board[r][c]='X'
            print("Bot hit your ship")
            print_board(player_board)
        else:
            player_board[r][c]='/'
            print("Bot missed")
            print_board(player_board)
            bot_in_turn=False

def check_winner():
    player_points=0
    bot_points=0
    for r in range(10):
        for c in range(10):
            if player_board[r][c]=='O':
                player_points+=1
            elif bot_board[r][c]=='O':
                bot_points+=1
    if player_points==0:
        print("Bot wins")
        return True
    elif bot_points==0:
        print("Player wins")
        return True
    return False

bot_ship(bot_board)
place_ship(player_board)
while check_winner() is False:
    player_turn()
    bot_turn()