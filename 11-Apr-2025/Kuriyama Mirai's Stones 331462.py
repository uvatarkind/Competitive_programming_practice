# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
given = list(map(int, input().split()))

prefix_given = [0] * (n + 1)
for i in range(n):
    prefix_given[i + 1] = prefix_given[i] + given[i]

cost = sorted(given)
prefix_cost = [0] * (n + 1)
for i in range(n):
    prefix_cost[i + 1] = prefix_cost[i] + cost[i]

question = int(input())
for _ in range(question):
    q = list(map(int, input().split()))
    l, r = q[1], q[2]
    if q[0] == 1:
        print(prefix_given[r] - prefix_given[l - 1])
    else:
        print(prefix_cost[r] - prefix_cost[l - 1])
