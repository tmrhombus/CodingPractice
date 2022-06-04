import solution as sol

maxn = 15

maxchain = sol.solution( maxn )

print("The longest Collatz chain made from a starting number {} < {}".format(maxchain[0],maxn))
print("  has {} terms".format(len(maxchain)))
print("  and is {}".format(maxchain))
