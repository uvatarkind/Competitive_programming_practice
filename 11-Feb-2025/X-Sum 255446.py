# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t= int(input())
for _ in range(t):
    n,m= list(map(int,input().split()))
    matrix=[]
    mx=0
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row) 
    def bound(l,r):
        return  0<=l<n and 0<=r<m
    direction=[[-1,1],[1,1],[-1,-1],[1,-1]]
    for i in range(n):
        for j in range(m):
            summ= matrix[i][j]
            for left,right in direction :
                    tempi=i+left
                    tempj=j+right
                    while bound(tempi,tempj):
                        summ+=matrix[tempi][tempj]
                        tempi +=left
                        tempj += right
            mx=max(mx,summ)
    print(mx)
                        