# Bubble sorting

def bubble_sort(list):
    if len(list) == 0:
        output = None
    elif len(list) == 1:
        output = list[0]
    else:
        copy_list = []
        for i_element in list:
            copy_list.append(i_element)
        number_of_elements = len(copy_list)
        while number_of_elements > 1:
            for i_index in range(number_of_elements-1):
                if copy_list[i_index] > copy_list[i_index+1]:
                    copy_list[i_index], copy_list[i_index+1] = copy_list[i_index+1], copy_list[i_index]
            number_of_elements = number_of_elements-1
        output = copy_list
       return output

list_ = [5, 1, 4, 7, 9, 3, 8, 2]
print(bubble_sort(list_))
