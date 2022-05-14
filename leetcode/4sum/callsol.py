import solution as sol

nums = [1,3,5,7,2,4,6,8,7,2,4,6,8]
target = 11

outlist = sol.solution( nums, target )

print("Initial list: \n {}".format(nums))
print("\n Target: {}".format(target))
print("\n Valid Combinations:")
for alist in outlist:
 print(" {}".format(alist))
