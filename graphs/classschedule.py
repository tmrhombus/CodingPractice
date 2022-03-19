
import topologicalsort as ts

numcourses = 4
prerequisites = [[2,0],[1,0],[3,1],[3,2]]

coursegraph = ts.Graph(numcourses)
for pair in prerequisites:
 coursegraph.addEdge(pair[1], pair[0])

courseorder = coursegraph.topologicalSort()

print(courseorder)
