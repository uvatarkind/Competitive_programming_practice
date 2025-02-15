# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t= int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    has=Counter(arr)
    mx=0
    maxsum=0
    new=Counter(has.values())
    sorted_data_desc = list(sorted(new.keys(), reverse=True))
    for key in sorted_data_desc:
        maxsum+=new[key]
        mx=max(mx,(key*maxsum))
    print(n-mx)