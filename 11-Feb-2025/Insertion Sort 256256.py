# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

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
    j = n - 2
    key = arr[n - 1]

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        print(" ".join(map(str, arr)))  # Print the array after each shift
        j -= 1
    arr[j + 1] = key
    print(" ".join(map(str, arr)))  # Print the array after placing the key

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
