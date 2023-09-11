# Drop non-dominants. The nested for loop below runs in O(n^2),
# and the other for loop runs in linear time, or O(n). This is
# technically O(n + n^2), but with Big O we can drop the n because
# we're only concerned about the worst case scenario

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)