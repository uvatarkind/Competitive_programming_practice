# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
summ = 0
mx = 0

while right < n:
    
    if summ + arr[right] <= t:
        summ += arr[right]
        right += 1
        mx = max(mx, right - left) 
    else:
        summ -= arr[left]
        left += 1  

print(mx)