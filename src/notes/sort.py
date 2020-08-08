# insertion sort

my_list = [8, 2, 5, 4, 1, 3]
temp = 2


# separate first element
# for all other items, start at second (index 1)
    # put current num into temp var
    # look left until we find correct postion
    # as we look left, shift items right
# when left is smaller than temp or we are at zero index, put at this location


def iterative_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        # put current num into tem 
        temp = list_to_sort[i]
        j = 1
        # look left until we find correct postion
        while j > 0 and temp < list_to_sort[j -1]:
            print(j)
            # as we look left, shift items right
            list_to_sort[j] = list_to_sort[j-1] # make postion at j the position 
            j -= 1
        list_to_sort[j] = temp
    return list_to_sort

iterative_sort(my_list)