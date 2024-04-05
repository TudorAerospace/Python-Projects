a = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
b = [["0,0", "0,1", "0,2"],
     ["1,0", "1,1", "1,2"],
     ["2,0", "2,1", "2,2"]]
from colorama import Fore


def draw_board():
    v = 0
    h = 0
    for k in range(3):
        for i in range(3):
            print(" ----", end="")
        print()
        h = 0
        for j in range(4):
            print(" | ", end="")
            for m in range(1):
                if j != 3:
                    if a[v][h] == "X":
                        print(Fore.RED + a[v][h] + Fore.RESET, end="")
                    elif a[v][h] == "O":
                        print(Fore.GREEN + a[v][h] + Fore.RESET, end="")
                    elif a[v][h] == 0:
                        print(a[v][h], end="")
                    if h != 2:
                        h = h + 1
                    else:
                        pass
                else:
                    pass
        if v != 2:
            v = v + 1
        else:
            pass
        print()
    for l in range(3):
        print(" ----", end="")
    print()


def win_conditions1(a):
    player1_win = False
    if a[0][0] == "X" and a[1][0] == "X" and a[2][0] == "X":
        player1_win = True
        return player1_win
    elif a[0][1] == "X" and a[1][1] == "X" and a[2][1] == "X":
        player1_win = True
        return player1_win
    elif a[0][2] == "X" and a[1][2] == "X" and a[2][2] == "X":
        player1_win = True
        return player1_win
    elif a[0][0] == "X" and a[0][1] == "X" and a[0][2] == "X":
        player1_win = True
        return player1_win
    elif a[1][0] == "X" and a[1][1] == "X" and a[1][2] == "X":
        player1_win = True
        return player1_win
    elif a[2][0] == "X" and a[2][1] == "X" and a[2][2] == "X":
        player1_win = True
        return player1_win
    elif a[0][0] == "X" and a[1][1] == "X" and a[2][2] == "X":
        player1_win = True
        return player1_win
    elif a[0][2] == "X" and a[1][1] == "X" and a[2][0] == "X":
        player1_win = True
        return player1_win


def win_conditions2(a):
    player2_win = False
    if a[0][0] == "O" and a[1][0] == "O" and a[2][0] == "O":
        player2_win = True
        return player2_win
    elif a[0][1] == "O" and a[1][1] == "O" and a[2][1] == "O":
        player2_win = True
        return player2_win
    elif a[0][2] == "O" and a[1][2] == "O" and a[2][2] == "O":
        player2_win = True
        return player2_win
    elif a[0][0] == "O" and a[0][1] == "O" and a[0][2] == "O":
        player2_win = True
        return player2_win
    elif a[1][0] == "O" and a[1][1] == "O" and a[1][2] == "O":
        player2_win = True
        return player2_win
    elif a[2][0] == "O" and a[2][1] == "O" and a[2][2] == "O":
        player2_win = True
        return player2_win
    elif a[0][0] == "O" and a[1][1] == "O" and a[2][2] == "O":
        player2_win = True
        return player2_win
    elif a[0][2] == "O" and a[1][1] == "O" and a[2][0] == "O":
        player2_win = True
        return player2_win


def player_input():
    player1_win = False
    player2_win = False
    draw = False
    while player1_win == False and player2_win == False and draw == False:
        for i in range(4):
            if win_conditions1(a):
                print("Player X wins!")
                player1_win = True
                break
            elif win_conditions2(a):
                player2_win = True
                print("Player O wins!")
                break
            elif not any(0 in sublist for sublist in a):
                print("Draw")
                draw = True
                break
            for j in range(5):
                if win_conditions1(a):
                    print("Player X wins!")
                    player1_win = True
                    break
                b = str(input("Please input Player X's position: "))
                c = b.split(",")
                d = int(c[0])
                e = int(c[1])
                if a[d][e] == 0:
                    a[d][e] = "X"
                    break
                else:
                    print("Please use an empty space.")
            draw_board()
            if win_conditions2(a):
                player2_win = True
                print("Player O wins!")
                break
            elif win_conditions1(a):
                player1_win = True
                print("Player X wins!")
                break
            elif not any(0 in sublist for sublist in a):
                print("Draw")
                draw = True
                break
            for j in range(4):
                if win_conditions2(a):
                    player2_win = True
                    print("Player O wins!")
                    break
                b = str(input("Please input Player O's position: "))
                c = b.split(",")
                d = int(c[0])
                e = int(c[1])
                if a[d][e] == 0:
                    a[d][e] = "O"
                    break
                else:
                    print("Please use an empty space.")
            draw_board()
            print("---------------------------------")


def draw_board_b():
    v = 0
    h = 0
    for k in range(3):
        for i in range(3):
            print(" ----- ", end="")
        print()
        h = 0
        for j in range(4):
            print(" | ", end="")
            for m in range(1):
                if j != 3:
                    print(b[v][h], end="")
                    if h != 2:
                        h = h + 1
                    else:
                        pass
                else:
                    pass
        if v != 2:
            v = v + 1
        else:
            pass
        print()
    for l in range(3):
        print(" ----- ", end="")
    print()


print("Welcome to Tic-Tac-Toe!")
print("Here is each possible move:")
draw_board_b()
print("-------------------------")
draw_board()

player_input()

input("Press Enter to exit...")
