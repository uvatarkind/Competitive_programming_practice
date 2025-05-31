# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

n, q = map(int, input().split())
parent = {i:i for i in range(1 , n + 1)}
parent[-1] = -1
def find(num):

    root = num
    while root != parent[root] :
        parent[root] = parent[parent[root]]
        root = parent[root]
        
    return parent[root]
    
for _ in range(q):
    query , num = input().split()
    num = int(num)
    if query == "?":
        print(find(num))

    else:
        if num == n:
            parent[n] = -1
            continue
        parent[find(num)] = find(num + 1)
