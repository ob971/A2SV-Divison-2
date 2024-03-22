# Read inputs
_ = input()  # Discard the first input
english_subs = set(map(int, input().split()))
_ = input()  # Discard the third input
french_subs = set(map(int, input().split()))

# Find students subscribed to at least one newspaper
total_subs = len(english_subs.union(french_subs))

# Output the total number of students subscribed to at least one newspaper
print(total_subs)
2
