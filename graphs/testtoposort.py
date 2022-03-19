
import topologicalsort as ts
 
g = ts.Graph(6)
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()

