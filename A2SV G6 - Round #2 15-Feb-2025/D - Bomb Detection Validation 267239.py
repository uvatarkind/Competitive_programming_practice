# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m= list(map(int,input().split()))
matrix=[]
for i in range(n):
    row=list(input())
    matrix.append(row)
def bound(l,r):
    return  0<=l<n and 0<=r<m
direction=[[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]
Valid=True
for i in range(n):
    for j in range(m):
        if matrix[i][j]=="*":
            continue
        else:
            count=0
            for left,right in direction:
                tempi=i+left
                tempj=j+right
                if bound(tempi,tempj):
                    if matrix[tempi][tempj]=="*":
                        count+=1
            if matrix[i][j]==".":
                if count!=0:
                    Valid=False
            else:
                if int(matrix[i][j])!= count:
                    Valid= False
if Valid:
    print("YES")
else:
    print("NO")
