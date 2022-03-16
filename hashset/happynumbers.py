# 
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
# 
# Return true if n is a happy number, and false if not.
# 
# Example:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

import myHashSet as mhs

def isithappy(thenumber):

 alreadyseen = mhs.HashSet()
 alreadyseen.add(thenumber)

 currentnumber = thenumber
 while True:
  # split the number into an array of digits
  digitized = [int(d) for d in str(currentnumber)]
  squaresum = 0
  for i in digitized:
   squaresum += i**2

  print("  Current Number: {}".format(currentnumber))
  print("   Digitized: {}".format(digitized))
  print("   Square Sum: {}".format(squaresum))

  if squaresum==1: return True

  if alreadyseen.contains(squaresum): break
  else:
   alreadyseen.add(squaresum)
   currentnumber = squaresum
   
 return False


numberstotest = [2,62,23452,773,19]
for mynumber in numberstotest:

 print("Testing number {}".format(mynumber))
 print("The number {} is happy: {}\n".format(mynumber, isithappy(mynumber)))
 
 
