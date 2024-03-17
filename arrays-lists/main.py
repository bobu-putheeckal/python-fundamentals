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

'''
Find Common Elements in Two Lists
'''
def common_elements(list1,list2):
    common = []
    largest = list1 if len(list1) > len(list2) else list2
    for element in largest:
        if element in list1 and element in list2:
            common.append(element)
    print(common)




# remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
common_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [ 6, 7, 16, 17, 18, 19, 20])