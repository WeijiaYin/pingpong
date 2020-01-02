def find_player_x(length, k12):
    player_x = list(range(0, length))
    for i in range(length):
        for j in range(length):
            if i != j:
                if k12[i][j] == 0:
                    player_x.remove(i)
                    break
    with open('playerX.txt', "w+") as f:
        for player in player_x:
            f.write(str(player))
            f.write('\t')
        f.close()
    return player_x

