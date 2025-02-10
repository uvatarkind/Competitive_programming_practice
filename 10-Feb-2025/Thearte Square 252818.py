# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math
n,m,a= map(int,input().split())
 
total= ((n+a-1)//a)*((m+a-1)//a)
print(total)