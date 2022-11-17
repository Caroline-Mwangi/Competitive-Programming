#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    sort_val = arr[-1]
    
    for i in reversed(range(1, n)):
        if arr[i-1] > sort_val:
            arr[i] = arr[i-1]
            print(*arr)
        else:
            arr[i] = sort_val
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
