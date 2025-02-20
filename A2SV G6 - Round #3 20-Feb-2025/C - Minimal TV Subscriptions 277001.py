# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter

t = int(input())  

for _ in range(t):
    n, k, d = map(int, input().split())  
    arr = list(map(int, input().split()))  

    if d > n:  
        print(len(set(arr)))  
        continue  

    show_count = Counter(arr[:d])  
    mn_subs = len(show_count)  

    left = 0
    for right in range(d, n):
       
        show_count[arr[left]] -= 1
        if show_count[arr[left]] == 0:
            del show_count[arr[left]]
        left += 1

       
        show_count[arr[right]] += 1
        
        
        mn_subs = min(mn_subs, len(show_count))

    print(mn_subs)
