# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t=int(input())
for _ in range(t):
    n= int(input())
    p=list(map(int,input().split()))
    i=1
    count=0
    while i<n:
        if p[i-1]>p[i]:
          count+=1
          i+=2
        else:
            i+=1
    print(count)
        
    