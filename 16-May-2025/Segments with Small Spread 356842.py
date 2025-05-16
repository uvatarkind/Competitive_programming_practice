# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

def count_good_segments(n, k, a):
    minq = deque()
    maxq = deque()
    res = 0
    l = 0

    for r in range(n):
        
        while minq and a[r] < a[minq[-1]]:
            minq.pop()
        minq.append(r)

        
        while maxq and a[r] > a[maxq[-1]]:
            maxq.pop()
        maxq.append(r)

      
        while a[maxq[0]] - a[minq[0]] > k:
            l += 1
            if minq[0] < l:
                minq.popleft()
            if maxq[0] < l:
                maxq.popleft()

        res += r - l + 1

    return res

print(count_good_segments(n, k, a))
