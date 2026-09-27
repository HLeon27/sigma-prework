my_list = [100, -100]


def max_min(array: list):
    longest = array[1]
    shortest = array[1]
    for i in array:
        if longest < i:
            longest = i
        if shortest > i:
            shortest = i
    return [shortest, longest]


print(max_min(my_list))
