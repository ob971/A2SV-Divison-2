# Read input
n, m = map(int, input().split())
group_a = {}

# Store indices of words in group A
for i in range(1, n + 1):
    word = input().strip()
    if word in group_a:
        group_a[word].append(i)
    else:
        group_a[word] = [i]

# Find indices of words in group B
for i in range(m):
    word = input().strip()
    if word in group_a:
        print(*group_a[word])
    else:
        print(-1)
