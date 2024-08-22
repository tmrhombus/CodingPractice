from solution import Solution

#intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[7,14],[4,8],[16,20],[17,18],[16,17]]

sol = Solution()

out = sol.merge(intervals)

print(f"In:  {intervals}")
print(f"Out: {out}")
