# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t= int(input())
for _ in range(t):
    s=input()
    n=len(s)
    if s[n-1]=='o':
        print('FILIPINO')
    elif s[n-1]=='u':
        print('JAPANESE')
    else:
        print('KOREAN')