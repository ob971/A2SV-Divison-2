if __name__ == '__main__':
    n = int(input())  # Number of elements in the tuple
    integer_list = sorted(map(int, input().split()))  # Space-separated integers as input, sorted
    
    # Create a tuple from the input integers
    tuple_input = tuple(integer_list)
    
    # Print the hash value of the tuple
    print(hash(tuple_input))
