# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    char=Counter(s)
    summ=0
    lc=len(char)
    new=set()
    
    for x in s:
        char[x]-=1
        new.add(x)
        if char[x]==0:
            del char[x]
        lc=max(lc,len(char)+len(new))
    print(lc) 