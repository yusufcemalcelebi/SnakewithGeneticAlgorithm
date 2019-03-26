import numpy as np
import random
import math
import matplotlib

def create_matrix(matrix_size, foodCount):
    matrix = np.zeros([matrix_size, matrix_size], dtype = int)
    for i in range(foodCount):
        matrix[random.randint(0,matrix_size-1)][random.randint(0,matrix_size-1)] = 1
    print(matrix)
    return matrix

def run_snake_run(stepCount,foodCount):
    status = 1          #1 live, 0 dead
    array = np.array()
    return array

create_matrix(10,7)