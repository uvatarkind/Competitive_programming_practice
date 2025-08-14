# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

import math
t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    d=list(map(int,input().split()))
    a=list(map(int,input().split()))
    low=1
    high= sum(d)
    def check(mid,d,a):
        i=0
        count=0
        for i in range(len(d)):
            if mid>=d[i]:
                count+=a[i]
            else:
                count+=(a[i]*(math.ceil(d[i]/mid)))
    
        if count <= h:
            return True
        else:
            return False
    ans=-1 
    while low<=high:
        mid=(low+high)//2
        
        if check(mid,d,a):
            high=mid-1
            ans=mid
        else:
            low=mid+1
    print(ans)


        