# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  data = set(s)
  char = ""
  mncnt = float("inf")
  
  for char in data:
    l, r = 0, n - 1
    cnt = 0
    x = 1
    
    while l < r:
      if s[l] == s[r]:
        l, r = l + 1, r - 1
        continue
      
      if s[l] != char and s[r] != char:
        x = 0
        break
    
      else:
        cnt += 1
        if s[l] == char:
          l += 1
        else:
          r -= 1
          
    if x:
      mncnt = min(mncnt, cnt)
      
  print(mncnt if mncnt != float("inf") else -1)