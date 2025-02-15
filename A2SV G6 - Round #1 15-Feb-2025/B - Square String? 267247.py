# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t=int(input())
for _ in range(t):
    s=input()
    if len(s)%2==1:
        print("NO")
    else:
        a= s[:len(s)//2]
        b= s[len(s)//2:]
        for i in range(len(a)):
            if a[i]!= b[i]:
                print("NO")
                break
        else:
            print("YES")
        
            
        