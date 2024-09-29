from solution import Solution 


#numbers = [2,7,11,15]
#target  = 9

#numbers = [-1,0,3,7,11,21,35,71]
#target  = 18

numbers = [1,2,2,3,5,6,6,13,14,15,16,17]
target  = 12

sol = Solution()
out = sol.twoSum(numbers, target)

print(f"numbers: {numbers}, target: {target}")
print(f"solution: {out}")
