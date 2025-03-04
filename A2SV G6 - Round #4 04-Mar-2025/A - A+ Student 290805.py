# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    ans=[]
    
    if a > b and a>c:
        ans.append(0)
    else:
        if b >= c:
           temp = b-a
           temp= temp+1
           ans.append(temp)
        else:
            temp = c-a
            temp= temp+1
            ans.append(temp)
            
    if b > a and b>c:
        ans.append(0)
    else:
        if a >= c:
           temp = a-b
           temp= temp+1
           ans.append(temp)
        else:
            temp = c-b
            temp= temp+1
            ans.append(temp)
    
    if c > b and c>a:
        ans.append(0)
    else:
        if b >= a:
           temp = b-c
           temp= temp+1
           ans.append(temp)
        else:
            temp = a-c
            temp= temp+1
            ans.append(temp)
    print(ans[0] ,ans [1], ans[2])