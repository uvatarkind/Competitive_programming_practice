# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))


initial_cost = a[-1] - a[0]

if k == 1:
    print(initial_cost)
else:
   
    diffs = []
    for i in range(1, n):
        diffs.append(a[i] - a[i - 1])
    
    diffs.sort(reverse=True)
    
    cost_reduction = sum(diffs[:k - 1])
    result = initial_cost - cost_reduction
    print(result)
