#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #for i in range(len(matrix)):
        #for j in range(len(matrix[i])):
            #print("{:d}".format(matrix[i][j]), end = "")
            #if j != len(matrix[i]) - 1:
                #print(" ", end = " ")
    x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix])
    print(x)
 #  for row in matrix:
       #for val in row:
          # print(val, end=" ")
      # print()
