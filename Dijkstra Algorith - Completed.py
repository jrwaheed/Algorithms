## Dijkstra Algorith practice
## Dont get tied up in how other people wrote their code
## Use your brain and focus on the concept and what needs to be accomplished.

##For this algorthm, the main point is to find the shortest distance for each node.
## Ultimately, you will find the shortest distance to the finish line. 
from collections import deque


matrix ={}
matrix["start"] ={}
matrix["alpha"] ={}
matrix["beta"] ={}
matrix["charlie"] ={}
matrix["delta"] ={}
matrix["finish"] = {}

matrix["start"]["start"] = 0
matrix["start"]["alpha"] = 5
matrix["start"]["beta"] = 2
matrix["alpha"]["charlie"] = 4
matrix["alpha"]["delta"] = 2
matrix["beta"]["alpha"] = 8 
matrix["beta"]["delta"] = 7
matrix["charlie"]["delta"] = 6
matrix["charlie"]["finish"] = 3
matrix["delta"]["finish"] = 1
matrix["finish"]["finish"] = 0

min_distance = float("inf")
processed_nodes = []
unvisited_nodes = ["start","alpha", "beta", "charlie", "delta","finish"]

## path_to_node means postion 1 is the destination, position 2 is the origin
path_to_node = { "start": "start",
                "alpha":"",
                "beta": "",
                "charlie": "",
                "delta": "",
                "finish": ""}


distance_fromStart ={"start": 0,
                "alpha": float("inf"),
                "beta": float("inf"),
                "charlie": float("inf"),
                "delta": float("inf"),
                "finish": float("inf")}




def find_the_fastest_node(distance_fromStart): ##Simply think!
    rabbit = 1000

    for node in distance_fromStart:
        if distance_fromStart.get(node) < rabbit and node not in processed_nodes:
            rabbit = distance_fromStart.get(node)
            min_distance_node = node
            
    processed_nodes.append(min_distance_node)
    unvisited_nodes.remove(min_distance_node)
    print(min_distance_node)
    
    return min_distance_node



while unvisited_nodes != []:
    min_distance_node = find_the_fastest_node(distance_fromStart)
    print(distance_fromStart)
    neighbors = []
    for node in matrix[min_distance_node].keys():
        neighbors.append(node)
        
    for neighbor_node in neighbors:
        if (distance_fromStart[min_distance_node] + matrix[min_distance_node][neighbor_node]) < distance_fromStart[neighbor_node]:
            distance_fromStart[neighbor_node] = (distance_fromStart[min_distance_node] + matrix[min_distance_node][neighbor_node]) ##Here is the magic. Not really that hard. 
            path_to_node[neighbor_node] = min_distance_node

print(distance_fromStart)
print(path_to_node)
