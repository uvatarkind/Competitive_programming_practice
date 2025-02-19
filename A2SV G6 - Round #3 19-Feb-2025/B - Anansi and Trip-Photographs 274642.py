# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t= int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    l=0
    r=n
    valid=True
    while l<r:
        if arr[r+l]-arr[l]<x:
            valid=False
        l+=1
    if valid:
        print("YES")
    else:
        print("NO")