import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic


def hillClimbing():
    graph = {
        'A' : Node('A', None, [('B',1)], 0, (0,0)), 
        'B' : Node('B', None, [('C',1), ('F',1), ('A',1)], 0,(1,0)), 
        'C' : Node('C', None, [ ('D',1), ('B',1)], 0,(2,0)), 
        'D' : Node('D', None, [('E',1), ('C',1)], 0,(3,0)), 
        'E' : Node('E', None, [('G',1), ('D',1)], 0,(4,0)), 
        'F' : Node('F', None, [('I',1), ('B',1)], 0,(1,1)), 
        'G' : Node('G', None, [('L',1), ('E',1)], 0,(4,1)), 
        'H' : Node('H', None, [('M',1), ('I',1)], 0,(0,2)), 
        'I' : Node('I', None, [ ('J',1), ('N',1), ('H',1)], 0,(1,2)), 
        'J' : Node('J', None, [('K',1), ('I',1)], 0,(2,2)), 
        'K' : Node('K', None, [('O',1), ('L',1), ('J',1)], 0,(3,2)), 
        'L' : Node('L', None, [('P',1), ('K',1), ('G',1)], 0,(4,2)), 
        'M' : Node('M', None, [('Q',1), ('N',1), ('H',1)], 0,(0,3)), 
        'N' : Node('N', None, [('R',1), ('I',1), ('M',1)], 0,(1,3)), 
        'O' : Node('O', None, [('P',1), ('K',1)], 0,(3,3)), 
        'P' : Node('P', None, [('O',1), ('L',1)], 0,(4,3)), 
        'Q' : Node('Q', None, [('T',1), ('R',1), ('M',1)], 0,(0,4)),
        'R':  Node('R', None, [('U',1), ('S',1), ('N',1), ('Q',1)], 0,(1,4)), 
        'S' : Node('S', None, [('V',1), ('R',1)], 0,(2,4)),        
        'T' : Node('T', None, [('U',1), ('Q',1)], 0,(0,5)), 
        'U' : Node('U', None, [('V',1), ('T',1), ('R',1)], 0,(1,5)), 
        'V' : Node('V', None, [('W',1), ( 'U',1), ('S',1)], 0,(2,5)), 
        'W' : Node('W', None, [('X',1), ('V',1)], 0,(3,5)), 
        'X' : Node('X', None, [('W',1)], 0,(4,5))
    }
    initialState = 'A'
    goalState = 'X'

    parentNode = initialState
    parentCost = math.sqrt((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])
                           ** 2 + (graph[goalState].heuristic[1] - graph[initialState].heuristic[1])**2)
    explored = []
    solution = []
    minChildCost = parentCost - 1
    while parentNode != goalState:
        bestnode = parentNode
        minChildCost = parentCost
        for child in graph[parentNode].actions:
            childCost = math.sqrt((graph[goalState].heuristic[0] - graph[child[0]].heuristic[0])**2 + (graph[goalState].heuristic[1] - graph[child[0]].heuristic[1])**2)
            if childCost < minChildCost:
                bestNode = child[0]
                minChildCost = childCost
        if bestNode == parentNode:
            break
        else:
            parentNode = bestNode
            parentCost = minChildCost
            solution.append(parentNode)
    return solution

solution = hillClimbing()
print(solution)