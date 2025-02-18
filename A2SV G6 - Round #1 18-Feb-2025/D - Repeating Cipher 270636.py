# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n=int(input())
s=input()
ans=""
c=1
i=0
while i<len(s):
    ans+=(s[i])
    c+=1
    i+=c
print(ans)