# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

t=int(input())
ans=""
for i in range(t+12):
    ans+=str(i)
print(ans[t])  