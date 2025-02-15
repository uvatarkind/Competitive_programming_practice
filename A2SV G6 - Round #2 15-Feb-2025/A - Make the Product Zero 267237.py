# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n=int(input())
mn=float("inf")
mx=float("-inf")
arr= list(map(int,input().split()))
for x in arr:
    if x<0:
        mx=max(x,mx)
    elif x>0:
        mn=min(mn,x)
    if x==0:
        print(0)
        exit()
                       
if mx*(-1)>=mn:
    print(mn)
elif mx*(-1)<mn:
    print(mx*(-1))