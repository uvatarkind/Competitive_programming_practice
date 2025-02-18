# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    n = input().strip()
    p = input().strip()
    
    it = iter(n)
    if not all(char in it for char in s):
        print("NO")
        continue 
    count_s = Counter(s)
    count_n = Counter(n)
    count_p = Counter(p)
    for char in count_n:
        required = count_n[char]
        available = count_s.get(char, 0) + count_p.get(char, 0)
        if required > available:
            print("NO")
            break
    else:
        print("YES")