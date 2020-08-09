import random
import time

# keywords for iterative solutions:unsorted, random
my_range = 100
my_size = 10

my_random = random.sample(range(my_range), my_size)
print(my_random) # [49, 74, 28, 52, 12, 45, 63, 56, 80, 10]

searching_for = 3

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

print(linear_search(my_random, searching_for))

#binary search 
# keywords for binary search solutions: sorted, ordered

def find_value_binary(arr, value):
    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:
        middle = (first + last) //2
        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                last = middle -1 
            else: 
                first = middle +1
    return found
arr1 = [1, 2, 3, 4, 5, 6, 7] 
target = 3

find_value_binary(arr1, target)