# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())
for _ in range(t):
    a, b = input().split()
    if a == b:
        print("=")
    else:
        if a[-1] == b[-1]:
            if len(a) > len(b):
                print(">" if a[-1] != "S" else "<")
            else:
                print("<" if a[-1] != "S" else ">")
        else: 
            if a[-1] == "S":
                print("<")
            elif a[-1] == "M" and b[-1] == "S":
                print(">")
            elif a[-1] == "L":
                print(">")
            else:
                print("<")
