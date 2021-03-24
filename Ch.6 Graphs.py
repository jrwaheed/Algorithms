## Graphs are used to find the shortest distance between two nodes.
## Here we are implementing a graph using a hashtable(dictionary)
## We are also using a queue
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"]= ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

print(graph)