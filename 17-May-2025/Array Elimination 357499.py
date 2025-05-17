# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

import math
from functools import reduce

def find_common_factors(arr):
    def gcd_of_list(numbers):
        return reduce(math.gcd, numbers)

    gcd = gcd_of_list(arr)

    common_factors = []
    for i in range(1, int(gcd**0.5) + 1):
        if gcd % i == 0:
            common_factors.append(i)
            if i != gcd // i:
                common_factors.append(gcd // i)

    return sorted(common_factors)

t = int(input())

for _ in range(t):
    count = [0] * 32
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    if all(x == 0 for x in arr):
        ans=[x for x in range(1,len(arr)+1)]
        print(*ans)
    else:
        new=[]
        for num in arr:
            for j in range(32):
                if num & (1 << j):
                    count[j] += 1

        for c in count:
            if c != 0:
                ans.append(c)

        new=find_common_factors(ans)
        print(*new)
