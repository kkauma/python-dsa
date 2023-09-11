# Drop constants
# This function runs O(n + n) times, or O(2n), but with Big O
# we drop the constant and just say the function runs 
# in O(n)

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)