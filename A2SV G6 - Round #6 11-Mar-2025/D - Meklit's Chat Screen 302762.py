# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

new_arr = deque()  
seen = set()  

for num in arr:
    if num not in seen:
        if len(new_arr) >= k:
            removed = new_arr.popleft() 
            seen.remove(removed) 
        new_arr.append(num)
        seen.add(num)

print(len(new_arr))
print(*reversed(new_arr))  
