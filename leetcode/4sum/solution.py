
#
#def solution( nums, target ):
# """
# Lists the unique sets of 4 elements in 
#  an input set (nums) which sum to target
#
# nums:   a list of integers
# target: the goal to reach in the sum
# """
#
# # object to be returned, list of lists
# outlist = []
#
# # check if solutions are possible
# if nums is None or len(nums)<4:
#  return outlist
# 
# # start by sorting the list and removing duplicates
# nums = sorted(set(nums))
# # n = index of final element in nums
# n = len(nums)-1
#
# """
# Idea behind algo:
# indexes of elements are i,j,k,l
# index of final element is n
#
# start with i=n-3, j=n-2, k=n-1, l=n
#
# if nums[i]+nums[j]+nums[k]+nums[l] < target:
#  i,j,k,l are all maxed out
#  no more combos will work
# if nums[i]+nums[j]+nums[k]+nums[l] = target:
#  add it to the collection, 
#
#
# """
#
# print(nums)
# print(nums[0])
# print(nums[n])
#
#
#
#
#
#

def solution( nums, target ):
    # Resultant list
    quadruplets = list()
    # Base condition
    if nums is None or len(nums) < 4:
        return quadruplets
    # Sort the array
    nums.sort()
    # Length of the array
    n = len(nums)
    # Loop for each element of the array
    for i in range(0, n - 3):
        # Check for skipping duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Reducing to three sum problem
        for j in range(i + 1, n - 2):
            # Check for skipping duplicates
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue
            # Left and right pointers
            k = j + 1
            l = n - 1
            # Reducing to two sum problem
            while k < l:
                current_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if current_sum < target:
                    k += 1
                elif current_sum > target:
                    l -= 1
                else:
                    quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return quadruplets




