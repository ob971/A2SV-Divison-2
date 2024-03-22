# Read the input set
set_a = set(map(int, input().split()))

# Read the number of other sets
n = int(input())

# Initialize a flag to check if set_a is a strict superset of all other sets
is_strict_superset = True

# Iterate through each other set
for _ in range(n):
    other_set = set(map(int, input().split()))
    
    # Check if other_set is a subset of set_a and not equal to set_a
    if not (other_set.issubset(set_a) and other_set != set_a):
        is_strict_superset = False
        break

# Print the result
print(is_strict_superset)
