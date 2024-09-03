from solution import Solution

#matrix_in = [[1,2,3],[4,5,6],[7,8,9]]
matrix_in = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

sol = Solution()

out = sol.spiralOrder(matrix=matrix_in)

print(f"In: {matrix_in}")
print(f"Out: {out}")
