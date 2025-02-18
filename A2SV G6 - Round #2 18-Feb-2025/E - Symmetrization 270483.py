# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    ans=0
    for i in range(n):
        row=list(map(int,input()))
        arr.append(row)
    for i in range(n):
        for j in range(n):
            temp=[arr[i][j],arr[j][n-i-1],arr[n-j-1][i],arr[n-i-1][n-j-1]]
            one_count=temp.count(1)
            zero_count=temp.count(0)
            ans+=min(one_count,zero_count)
    print(ans//4)    