
#!/bin/python3

import math
import os
import random
import re
import sys

def squares(a, b):
    Ammount = 0
    for i in range(a, b):
        if i**0.5 // 1 == 0:
            Ammount += 1
    return(Ammount)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
