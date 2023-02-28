class Node:
    def __init__(self, state, parent, actions, pathCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.pathCost = pathCost
        
def actionSequence(graph, initialState, goalState):
    # list of connected paths
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution
    
def DFS():
    initialState = 'Arad'
    goalState = 'Bucharest'
    
    graph = {
        'Oradea': Node('Oradea', None, ['Zerind', 'Sibiu'], None),
        'Zerind': Node('Zerind', None, ['Oradea', 'Arad'], None),
        'Arad': Node('Arad', None, ['Zerind', 'Sibiu', 'Timnisoara'], None),
        'Sibiu': Node('Sibiu', None, ['Arad', 'Fagaras', 'Rimnicu Vilcea'], None),
        'Timnisoara': Node('Timnisoara', None, ['Arad', 'Lugoj'], None),
        'Fagaras': Node('Fagaras', None, ['Sibiu', 'Bucharest'], None),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, ['Sibiu', 'Pitesti', 'Craiova'], None),
        'Lugoj': Node('Lugoj', None, ['Timnisoara', 'Mehadia'], None),
        'Mehadia': Node('Mehadia', None, ['Lugoj', 'Drobeta'], None),
        'Drobeta': Node('Drobeta', None, ['Mehadia', 'Craiova'], None),
        'Craiova': Node('Craiova', None, ['Drobeta', 'Rimnicu Vilcea', 'Bucharest'], None),
        'Pitesti': Node('Pitesti', None, ['Rimnicu Vilcea', 'Bucharest'], None),
        'Bucharest': Node('Bucharest', None, ['Pitesti', 'Fagaras', 'Giurgia', 'Urziceni'], None),
        'Giurgia': Node('Giurgia', None, ['Bucharest'], None),
        'Urziceni': Node('Urziceni', None, ['Bucharest', 'Vaslui', 'Hirsova'], None),
        'Hirsova': Node('Hirsova', None, ['Urziceni', 'Eforie'], None),
        'Eforie': Node('Eforie', None, ['Hirsova'], None),
        'Vaslui': Node('Vaslui', None, ['Urziceni', 'Iasi'], None),
        'Iasi': Node('Iasi', None, ['Vaslui', 'Neamt'], None),
        'Neamt': Node('Neamt', None, ['Iasi'], None)
    }
    
    frontier = [initialState]
    explored = []
    
    while len(frontier) != 0:
        currentNode = frontier.pop(len(frontier) - 1)
        print(currentNode)
        explored.append(currentNode)
        currentChildren = 0
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    print(explored)
                    return actionSequence(graph,initialState,goalState)
                currentChildren = currentChildren + 1
                frontier.append(child)
        if currentChildren == 0:
            del explored[len(explored) - 1]

            
solution = DFS()
print(solution)