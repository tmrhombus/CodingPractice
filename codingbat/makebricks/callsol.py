
import solution as sol

nl = 4
nb = 2
goal = 11


ispossible = sol.solution(nl, nb, goal)

print("Nr. little bricks: {}".format(nl))
print("Nr. big bricks:    {}".format(nb))
print("Goal:  {}  is possible: {}".format(goal,ispossible))

