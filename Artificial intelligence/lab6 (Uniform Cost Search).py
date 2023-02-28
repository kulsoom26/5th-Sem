import math

def findMin(frontier):
    #return that node in the frontier which has a lowest cost
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier [i][1]:
            minV = frontier[i][1]
            node = i
    return node

def actionSequence (graph, initialState, goalState):
    #returns a list of states starting from goal state moving upwards towards 
    #parents until root node is reached 
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

class Node:
    #state = state 
    #class variable shared by all instances
    def __init__ (self, state, parent, actions, totalCost):
        self.state = state    #instance variable unique to each instance
        self.parent = parent 
        self.actions = actions    #we are not saving actions themselves, only output states of those actions
        self.totalCost = totalCost
        
def UCS():
    initialState = 'Arad'
    goalState = 'Bucharest'
    
    #we think of a graph as a dictionary, items comprise of nodes, where
    #each node has a key and a value, key is simply the state of the node 
    #and value are actual attributes that node object
    
    graph = {
        'Arad' : Node('Arad',None,[('Zerind',75),('Sibiu',140),('Timisoara',118)],0),
        'Oradea' : Node('Oradea',None,[('Zerind',71),('Sibiu',151)],0),
        'Zerind' : Node('Zerind',None,[('Arad',75),('Oradea',71)],0),
        'Timisoara' : Node('Timisoara',None,[('Lugoj',111),('Arad',118)],0),
        'Lugoj' : Node('Lugoj',None,[('Timisoara',111),('Mehadia',70)],0),
        'Mehadia' : Node('Mehadia',None,[('Lugoj',70),('Drobeta',75)],0),
        'Drobeta' : Node('Drobeta',None,[('Mehadia',75),('Craiova',120)],0),
        'Craiova' : Node('Craiova',None,[('Drobeta',120),('Pitesti',138),('Rimnicu Vilcea',146)],0), 
        'Rimnicu Vilcea' : Node('Rimnicu Vilecea',None,[('Sibiu',80),('Pitesti',97),('Craiova',146)],0),  
        'Sibiu' : Node('Sibiu',None,[('Rimnicu Vilcea',80),('Oradea',151),('Arad',140),('Fagaras',99)],0),  
        'Fagaras' : Node('Fagaras',None,[('Sibiu',99),('Bucharest',211)],0),
        'Pitesti' : Node('Pitesti',None,[('Rimnicu Vilcea',97),('Bucharest',101),('Craiova',138)],0),
        'Bucharest' : Node('Bucharest',None,[('Pitesti',101),('Giurgiu',90),('Urziceni',85),('Fagaras',211)],0),
        'Urziceni' : Node('Urziceni',None,[('Hirsova',98),('Bucharest',85),('Vaslui',142)],0),
        'Hirsova' : Node('Hirsova',None,[('Eforie',86),('Urziceni',98)],0),
        'Eforie' : Node('Eforie',None,[('Hirsova',86)],0),        
        'Vaslui' : Node('Vaslui',None,[('Urziceni',142),('Iasi',92)],0), 
        'Iasi' : Node('Iasi',None,[('Vaslui',92),('Neamt',87)],0), 
        'Neamt' : Node('Neamt',None,[('Iasi',87)],0),
        'Giurgiu' : Node('Giurgiu',None,[('Bucharest',90)],0)
    }
    frontier = dict()
    frontier[initialState] = (None, 0)
    explored = []    #parent of initial node is None and its cost is 0
    
    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]

solution = UCS()
print(solution)