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

'''
Sort a List of integers in highest to lowest
'''
def sort_list(list):
    list.sort(reverse=True)
    print(list)
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''
def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result =[]
        counter = 0
        for num in nums:
            pos = nums.index(target - num)
            if(pos!=0):
                result.append(counter)
                result.append(pos)
                break
            counter +=1
        return result


# remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# common_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [ 6, 7, 16, 17, 18, 19, 20])
# sort_list([17,18,5,4,6,1])
# print(twoSum([2, 7, 11, 15], 9)) # [0, 1]
# print(twoSum([3,2,4], 6)) 
print(twoSum([3,3], 6)) 