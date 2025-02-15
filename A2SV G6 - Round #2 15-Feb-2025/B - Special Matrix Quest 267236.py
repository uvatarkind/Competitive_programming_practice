# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n= int(input())
matrix=[]
sumupperD=0
sumlowerD=0
colsum=0
rowsum=0
middlenum=0
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if i==n//2:
            rowsum+=matrix[i][j]
        if j==n//2:
            colsum+=matrix[i][j]
        if i==j:
            sumupperD+=matrix[i][j]
        if i+j==n-1:
            sumlowerD+=matrix[i][j]
        if i==n//2 and j==n//2:
            middlenum+=matrix[i][j]
total= sumlowerD + sumupperD + rowsum + colsum-(middlenum*3)
print(total)
    
        
    