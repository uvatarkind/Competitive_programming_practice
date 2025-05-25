# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = int(input())
parents = [int(input()) for _ in range(n - 1)]

from collections import defaultdict

# Build tree
children = defaultdict(list)
for i, p in enumerate(parents):
    child = i + 2  # nodes are 1-indexed; first child is node 2
    children[p].append(child)

is_spruce = True

for node in range(1, n + 1):
    if node in children:  # it's a non-leaf
        leaf_count = sum(1 for child in children[node] if child not in children)
        if leaf_count < 3:
            is_spruce = False
            break

print("Yes" if is_spruce else "No")
