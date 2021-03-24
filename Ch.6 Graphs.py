## Graphs are used to find the shortest distance between two nodes.
## Here we are implementing a graph using a hashtable(dictionary)
## We are also using a queue

from collections import deque

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
searchQueue = deque()
searchQueue += graph["you"]

def personIsSeller(name):
    return name[-1] == "m"

while searchQueue:
    person = searchQueue.popleft()
    if personIsSeller(person):
        print(person + " is a mango seller")

    else:
        searchQueue += graph[person]


