import math
import os
import random
import re
import sys


matrix = []

first_multiple_input = input().rstrip().split()
for i in range(1,3):
    for j in range(1,2):
        matrix.append(first_multiple_input[j][i])
print(matrix)
