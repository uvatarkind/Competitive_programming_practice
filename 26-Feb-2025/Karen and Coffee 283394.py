# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
n , k ,d = integers()
recp = []
ans = 0
for i in range(n):
    left, right = integers()
    recp.append([left , right])
que = []
for i in range(d):
    left, right = integers()
    que.append([left, right]) 

mn , mx = float('inf') , 0
for left, right in recp:
    mn = min(mn , left)
    mx = max(mx , right)

ran = mx - mn + 1
prefix = [0] *(ran + 1)

for left, right in recp :
    prefix[left - mn] += 1
    if right - mn + 1 < ran:
        prefix[right - mn +1] -= 1
    
for i in range(1,ran):
    prefix[i] += prefix[i-1]

for i in range(ran):
    if prefix[i] >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0
for i in range(1,ran):
    prefix[i] += prefix[i-1]

for left, right in que:
    tag = 0
    if left < mn:
        left = mn
    if right > mx:
        right= mx
    if right < mn or left > mx :
        print(0)
    else:
        print(prefix[right - mn] -prefix[left - mn -1])