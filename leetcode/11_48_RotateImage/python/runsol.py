from solution import Solution 

matrix = [
 [11,12,13,14],
 [21,22,23,24],
 [31,32,33,34],
 [41,42,43,44]
]

matrix = [
[11,12,13],
[21,22,23],
[31,32,33]
]


matrix = [
[11,12,13,14,15],
[21,22,23,24,25],
[31,32,33,34,35],
[41,42,43,44,45],
[51,52,53,54,55]
]

#print(matrix)
for i in range(len(matrix)):
 print(matrix[i])

sol = Solution()
sol.rotate(matrix)

print("")
for i in range(len(matrix)):
 print(matrix[i])
