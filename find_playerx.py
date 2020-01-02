def find_player_x(matrix, k12):
    player_x = list(range(0, len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
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