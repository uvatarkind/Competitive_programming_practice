# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t=int(input())
for _ in range(t):
    x=int(input())
    if x==1:
        print(3)
    else:
        if x>0 and x&(x-1)==0:
            print(x+1)
        else:
            for i in range(32):
                if x & (1<<i):
                    print(1<<i)
                    break