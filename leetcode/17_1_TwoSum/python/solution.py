from typing import List
#from sortedcontainers import SortedDict
from collections import OrderedDict


class Solution:
 def twoSum(self, nums: List[int], target: int) -> List[int]:
        
  dict_nums = {}
  l = len(nums)
  for i in range(l):
   dict_nums[ nums[i] ] = i

  for i in range(l):
   j = target - nums[i]

   if (j in dict_nums) and (dict_nums[j] != i):
    return [i, dict_nums[j]]


## nicer version I didn't write

#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        seen = {}
#        for i, num in enumerate(nums):
#            complement = target - num
#            if complement in seen:
#                return [seen[complement], i]
#            seen[num] = i

  #s_nums = sorted(nums)

  #print(f"nums:  {nums}")
  #print(f"d_nums: {dict_nums}")
  #print(f"s_nums: {s_nums}")

#  i = 0
#  j = 1
#  while True:
#   print(f"i: {i}, j: {j}, s_i: {s_nums[i]}, s_j: {s_nums[j]}")
#   if ( s_nums[i] + s_nums[j] == target ):
#    return [dict_nums[s_nums[i]], dict_nums[s_nums[j]] ]
#   elif( s_nums[i] + s_nums[j] < target ):
#    j += 1 
#   else:
#    j -= 1
#    i += 1 
#  return [1]




#class Solution:
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#        
#  dict_nums = {}
#  l = len(nums)
#  for i in range(l):
#   dict_nums[ nums[i] ] = i
#   #dict_nums[nums[i]] = i
#
#  s_nums = sorted(nums)
#
#  print(f"nums:  {nums}")
#  print(f"d_nums: {dict_nums}")
#  print(f"s_nums: {s_nums}")
#
#  i = 0
#  j = 1
#  while True:
#   print(f"i: {i}, j: {j}, s_i: {s_nums[i]}, s_j: {s_nums[j]}")
#   if ( s_nums[i] + s_nums[j] == target ):
#    return [dict_nums[s_nums[i]], dict_nums[s_nums[j]] ]
#   elif( s_nums[i] + s_nums[j] < target ):
#    j += 1 
#   else:
#    j -= 1
#    i += 1 




  #odict_nums = OrderedDict(sorted(dict_nums.items(), key=lambda item: item[1] ))

  #dict(sorted(x.items(), key=lambda item: item[1]))

  #odict_nums = OrderedDict(sorted(dict_nums.keys()))
  #odict_nums = OrderedDict(sorted(dict_nums))

  #print(odict_nums)

  #i = 0
  #j = 1
  #while True:
  # if( odict_nums[i]+odict_nums[j] == 

  ##print(dict_nums)

  #for key in OrderedDict(sorted(dict_nums.items())):
  # print(f"{key} {dict_nums[key]}")

  #out = [i,j]

  return [1,2]
 
