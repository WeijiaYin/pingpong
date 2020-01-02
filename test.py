import unittest
import readFile
import generate
import strassen
import find_playerx
import numpy as np


class Test(unittest.TestCase):

    def test_read_matrix_from_file(self):
        # given
        expected = np.array([[0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 0, 0]])
        file_path = 'test_read_file.txt'
        # when
        matrix = readFile.input_matrix(file_path)
        # then
        self.assertTrue((matrix==expected).all())

    def test_generate_matrix(self):
        # given
        expected = 9
        input_number = 9
        # when
        matrix = generate.generate_matrix(input_number)
        # then
        self.assertEqual(len(matrix), expected)

    def test_strassen(self):
        # given
        input_matrix = np.array([[0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 0, 0]])
        expected = np.array([[0, 0, 0, 0, 1, 0, 0, 0], [2, 0, 2, 0, 2, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [2, 1, 2, 0, 2, 0, 1 ,0], [0, 0, 1, 0, 0, 0, 0, 0], [3, 1, 3, 2, 3, 0, 0, 0], [3, 0, 3, 1, 3, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        # when
        matrix = strassen.strassen(input_matrix, input_matrix)
        # then
        self.assertTrue((matrix == expected).all())

    def test_addition(self):
        # given
        input_matrix1 = np.array([[0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 1,0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1, 0],
 [1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        input_matrix2 = np.array([[0, 0, 0, 0, 1, 0, 0, 0], [2, 0, 2, 0, 2, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [2, 1, 2, 0, 2, 0, 1 ,0], [0, 0, 1, 0, 0, 0, 0, 0], [3, 1, 3, 2, 3, 0, 0, 0], [3, 0, 3, 1, 3, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        expected = np.array([[0, 0, 1, 0, 1, 0, 0, 0], [3, 0, 3, 1, 3, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [3, 1, 3, 0, 3, 1, 1, 0], [1, 0, 1, 0, 0, 0, 0, 0], [4, 2, 4, 2, 4, 0, 1, 0], [4, 1, 4, 2, 4, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        # when
        matrix = np.array(strassen.matrix_addition(input_matrix1, input_matrix2))
        # then
        self.assertTrue((matrix == expected).all())

    def test_find_playerX(self):
        # given
        expected = [3, 5, 6]
        input_length = 7
        input_matrix = np.array([[0, 0, 1, 0, 1, 0, 0, 0], [3, 0, 3, 1, 3, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [3, 1, 3, 0, 3, 1, 1, 0], [1, 0, 1, 0, 0, 0, 0, 0], [4, 2, 4, 2, 4, 0, 1, 0], [4, 1, 4, 2, 4, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        # when
        result = find_playerx.find_player_x(input_length, input_matrix)
        # then
        self.assertEqual(result, expected)

