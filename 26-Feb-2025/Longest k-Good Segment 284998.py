# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

import sys,random,cmath
from collections import defaultdict, Counter


xors = random.randint(1, 1000000000)
con = lambda x: x^xors
number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'

def solve():
    n,k = numbers()
    nums = numbers()
    s = defaultdict(int)
    l = 0
    res = 0
    rest = [0,0]
    for r in range(len(nums)):
        s[nums[r]] += 1
        while l<=r and len(s) > k:
            s[nums[l]] -= 1
            if s[nums[l]] < 1:
                s.pop(nums[l],None)
            l+=1
        if len(s) <= k and r-l+1>res:
            res = max(res,r-l+1)
            rest = [l+1,r+1]

    print(*rest)
    return

solve()
