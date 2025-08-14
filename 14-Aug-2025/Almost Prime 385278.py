# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n= int(input())

prime_factors_count=[0]*(n+1)

for i in range(2,n+1):
    if prime_factors_count[i]==0:
        for j in range(i, n+1,i):
            prime_factors_count[j]+=1

count_almost_primes =sum(1 for i in range(1,n+1) if prime_factors_count[i]==2)
print(count_almost_primes)