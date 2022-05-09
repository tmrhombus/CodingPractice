
import solution as sol

nl = 10
nb = 2
goal = 16


ispossible = sol.solution(nl, nb, goal)

print("Nr. little bricks: {}".format(nl))
print("Nr. big bricks:    {}".format(nb))
print("Goal:  {}  is possible: {}".format(goal,ispossible))

