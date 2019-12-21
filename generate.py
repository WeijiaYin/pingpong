import numpy as np
def generate_matrix(num_player):
    player_matrix = np.zeros([num_player, num_player], dtype='int')
    for i in range(num_player):
        for j in range(i,num_player):
            if i!=j:
                player_matrix[i][j] = np.random.randint(0,2)
                player_matrix[j][i] = 1-player_matrix[i][j]
    return player_matrix

