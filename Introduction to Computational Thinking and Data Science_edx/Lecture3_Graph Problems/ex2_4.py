from lecture3Segment2 import *

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# Write the code that adds the appropriate edges to the graph
# in this box.

edges = []
edges.append(Edge(nodes[0],nodes[1]))
edges.append(Edge(nodes[1],nodes[4]))
edges.append(Edge(nodes[2],nodes[0]))
edges.append(Edge(nodes[3],nodes[2]))
edges.append(Edge(nodes[4],nodes[5]))
edges.append(Edge(nodes[5],nodes[3]))

for n in edges:
    g.addEdge(n)

# x=edges[0]
# print(x)
#something seems funny about this exercise but it passes the test so i leave it
