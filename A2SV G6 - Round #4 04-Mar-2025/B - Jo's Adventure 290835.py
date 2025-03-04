# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))


damage_right = [0] * n
for i in range(1, n):
    if arr[i] < arr[i - 1]: 
        damage_right[i] = damage_right[i - 1] + (arr[i - 1] - arr[i])
    else:
        damage_right[i] = damage_right[i - 1]


damage_left = [0] * n
for i in range(n - 2, -1, -1):
    if arr[i] < arr[i + 1]:  
        damage_left[i] = damage_left[i + 1] + (arr[i + 1] - arr[i])
    else:
        damage_left[i] = damage_left[i + 1]


for _ in range(m):
    sj, tj = map(int, input().split())
    if sj < tj:  
        print(damage_right[tj - 1] - damage_right[sj - 1])
    else:  
        print(damage_left[tj - 1] - damage_left[sj - 1])
