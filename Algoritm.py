# тандап сорттоо

# nums = [12, 8, 3, 20, 11]
#
#
# for i in range(len(nums)):
#     lowest_value_index = i
#     for j in range(i + 1, len(nums)):
#         if nums[j] < nums[lowest_value_index]:
#             lowest_value_index = j
#     nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
# print(nums)


### binary search ###

# def binarySearch(array, x):
#     low = 0
#     high = len(array)-1
#
#     while low <= high:
#         mid = low + (high - low)//2
#         if array[mid] == x:
#             return mid
#         elif array[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x)
# if result != -1:
#     print("index " + str(result))
# else:
#     print("Not found")