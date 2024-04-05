a =[[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

player1_win = False
player2_win = False

if a[0][0] & a[1][0] & a[2][0] == 1:
    player1_win = True
    pass
elif a[0][1] & a[1][1] & a[2][1] == 1:
    player1_win = True
    pass
elif a[0][2] & a[1][2] & a[2][2] == 1:
    player1_win = True
    pass
elif a[0][0] & a[0][1] & a[0][2] == 1:
    player1_win = True
    pass
elif a[1][0] & a[1][1] & a[1][2] == 1:
    player1_win = True
    pass
elif a[2][0] & a[2][1] & a[2][2] == 1:
    player1_win = True
    pass
elif a[0][0] & a[1][1] & a[2][2] == 1:
    player1_win = True
    pass
elif a[0][2] & a[1][1] & a[2][2] == 1:
    player1_win = True
    pass
elif a[0][0] & a[1][0] & a[2][0] == 2:
    player2_win = True
    pass
elif a[0][1] & a[1][1] & a[2][1] == 2:
    player2_win = True
    pass
elif a[0][2] & a[1][2] & a[2][2] == 2:
    player2_win = True
    pass
elif a[0][0] & a[0][1] & a[0][2] == 2:
    player2_win = True
    pass
elif a[1][0] & a[1][1] & a[1][2] == 2:
    player2_win = True
    pass
elif a[2][0] & a[2][1] & a[2][2] == 2:
    player2_win = True
    pass
elif a[0][0] & a[1][1] & a[2][2] == 2:
    player2_win = True
    pass
elif a[0][2] & a[1][1] & a[2][2] == 2:
    player2_win = True
    pass


if player1_win == True:
    print("Player 1 wins")
elif player2_win == True:
    print("Player 2 wins")
elif player1_win == False & player2_win == False:
    print("Draw")