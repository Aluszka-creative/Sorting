# Returns the biggest element from a list
def max(list):

    if len(list) == 0:
        output = None
    elif len(list) == 1:
        output = list[0]
    else:
        biggest = list[0]

        for i_item in list:
            if i_item >= biggest:
                biggest = i_item

        output = biggest
     return output

# Returns the smallest element from a list
def min(list):
    if len(list) == 0:
        output = None
    elif len(list) == 1:
        output = list[0]
    else:
        smallest = list[0]
        for i_item in list:
            if i_item < smallest:
                smallest = i_item
        output = smallest
    return output

# Function which checks if element is in the list
def contains(list, x):
    for i_item in list:
        if i_item == x:
            output = 1
    output = 0
    return output

def sort(list, from_bigger_or_smaller):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        if from_bigger_or_smaller == 'from_bigger':
            copy_list = []
            sorted_list = []
            for i_element in list:
                copy_list.append(i_element)
            for i_index in range(0, len(list)):
                max_element = max(copy_list)
                sorted_list.append(max_element)
                copy_list.remove(max_element)
            return sorted_list
        elif from_bigger_or_smaller == 'from_smaller':
            copy_list = []
            sorted_list = []
            for i_element in list:
                copy_list.append(i_element)
            for i_index in range(0, len(list)):
                min_element = min(copy_list)
                sorted_list.append(min_element)
                copy_list.remove(min_element)
            return sorted_list






list_ = [3, 5, 4, 1, 3]
print(sort(list_, 'from_smaller'))
