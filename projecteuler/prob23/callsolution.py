
import solution as sol

topnum = 100

thesum,nonexpressable = sol.solution(topnum)

print("The sum of all integers under {} which can not be written as the sum of two abundant numbers is {}".format(topnum, thesum))
print("The list of nonexpressable numbers is:\n {}".format(nonexpressable))
