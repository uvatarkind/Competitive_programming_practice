# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t=int(input())
for _ in range(t):
    n= int(input())
    r=list(map(int,input().split()))
    m= int(input())
    b=list(map(int,input().split()))
    
    def max_pref(a):
        mx=0
        curr=0
        for num in a:
            curr+=num
            mx=max(mx,curr)
       
        return mx
        
    
    red= max_pref(r)
    blue=max_pref(b)
    
    print(max(red,blue,red+blue))
