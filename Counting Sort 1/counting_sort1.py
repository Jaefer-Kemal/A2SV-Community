#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr,n):
    mm = max(arr)
    freq = [0] * 100
    for i in range(n):
        f = arr[i]
        freq[f] += 1
        
    return freq
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
