# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

import math
def sign(num):
    return num > 0
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    left = 0
    while left < n:
        right = left
        current_max = arr[left]
        while right < n and sign(arr[right]) == sign(arr[left]):
            current_max = max(current_max, arr[right])
            right += 1
        max_sum += current_max
        left = right
    
    print(max_sum)