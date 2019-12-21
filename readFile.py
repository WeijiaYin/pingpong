import numpy as np
def input_matrix(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
        player_matrix = np.zeros((len(lines), len(lines)), dtype='int')
        count = 0
        for line in lines:
            list = line.strip('\n').split(' ')
            player_matrix[count:] = list
            count+=1
    return player_matrix
