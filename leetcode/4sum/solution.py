

def solution( nums, target ):
 """
 Lists the unique sets of 4 elements in 
  an input set (nums) which sum to target

 nums:   a list of integers
 target: the goal to reach in the sum
 """

 # object to be returned, list of lists
 outlist = []

 # check if solutions are possible
 if nums is None or len(nums)<4:
  return outlist
 
 # start by sorting the list
 nums = sorted(set(nums))
 # n = index of final element in nums
 n = len(nums)-1

 """
 Idea behind algo:
 indexes of elements are i,j,k,l
 index of final element is n

 start with i=0, j=1,k=
 """

 print(nums)
 print(nums[0])
 print(nums[n])
