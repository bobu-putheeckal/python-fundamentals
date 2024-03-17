'''
When we have a list with elements, sometimes we need to remove duplicate elements, 
i.e., if the same element appears more than once, we only want to keep one copy of it.
'''
def remove_duplicates(input_list):
    output_list = []
    for list_element in input_list:
        # print (list_element)
        if list_element not in output_list:
            output_list.append(list_element)
    print(output_list)


remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])