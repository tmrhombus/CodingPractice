

def solution( nums, target ):
 """
 Lists the unique sets of 4 elements in 
  an input set (nums) which sum to target

 nums:   a list of integers
 target: the goal to reach in the sum
 """

 # object to be returned, list of lists
 outlist = []
 
 # start by sorting the list
 nums.sort()
 n = len(nums)


 print(nums)
 print(nums[0])
 print(nums[n-1])
