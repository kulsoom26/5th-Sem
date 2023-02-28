class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while( currentParent != None):
        solution.append(currentParent)
        currentParent = graph[currentParent].parent

    solution.reverse()
    return solution


def BFS():
    initialState ='1'
    goalState ='67'
    graph = {
        '1': Node('1', None, ['2', '9'], None),
        '2': Node('2', None, ['1', '3', '10'], None),
        '3': Node('3', None, ['2', '4', '11'], None),
        '4': Node('4', None, ['3', '5'], None),
        '5': Node('5', None, ['4', '6'], None),
        '6': Node('6', None, ['5'], None),
        '7': Node('7', None, ['8'], None),
        '8': Node('8', None, ['7', '13'], None),
        '9': Node('9', None, ['1','10', '15'], None),
        '10': Node('10', None, ['2', '9', '11'], None),
        '11': Node('11', None, ['3', '10', '16'], None),
        '12': Node('12', None, ['19'], None),
        '13': Node('13', None, ['8', '14', '20'], None),
        '14': Node('14', None, ['13'], None),
        '15': Node('15', None, ['9', '21'], None),
        '16': Node('16', None, ['11', '17'], None),
        '17': Node('17', None, ['16', '23'], None),
        '18': Node('18', None, ['19', '25'], None),
        '19': Node('19', None, ['12', '18'], None),
        '20': Node('20', None, ['13'], None),
        '21': Node('21', None, ['15', '22'], None),
        '22': Node('22', None, ['21', '26'], None),
        '23': Node('23', None, ['17', '24'], None),
        '24': Node('24', None, ['23', '25', '28'], None),
        '25': Node('25', None, ['18', '24'], None),
        '26': Node('26', None, ['22', '27', '32'], None),
        '27': Node('27', None, ['26', '33'], None),
        '28': Node('28', None, ['24', '35'], None),
        '29': Node('29', None, ['30', '36'], None),
        '30': Node('30', None, ['29', '37'], None),
        '31': Node('31', None, ['32', '39'], None),
        '32': Node('32', None, ['26', '31', '33'], None),
        '33': Node('33', None, ['27', '32', '34'], None),
        '34': Node('34', None, ['33', '35', '40'], None),
        '35': Node('35', None, ['28', '34', '41'], None),
        '36': Node('36', None, ['29', '37', '43'], None),
        '37': Node('37', None, ['30', '36', '38', '44'], None),
        '38': Node('38', None, ['37', '45'], None),
        '39': Node('39', None, ['31', '46'], None),
        '40': Node('40', None, ['34', '41', '47'], None),
        '41': Node('41', None, ['35', '40', '48'], None),
        '42': Node('42', None, ['43', '50'], None),
        '43': Node('43', None, ['36', '44', '51'], None),
        '44': Node('44', None, ['37', '43', '45', '52'], None),
        '45': Node('45', None, ['38', '44', '53'], None),
        '46': Node('46', None, ['39', '54'], None),
        '47': Node('47', None, ['40', '48'], None),
        '48': Node('48', None, ['41', '49', '57'], None),
        '49': Node('49', None, ['48', '50'], None),
        '50': Node('50', None, ['42', '49', '51', '58'], None),
        '51': Node('51', None, ['43', '50', '52', '59'], None),
        '52': Node('52', None, ['44', '51', '53', '60'], None),
        '53': Node('53', None, ['45', '52'], None),
        '54': Node('54', None, ['46', '55', '61'], None),
        '55': Node('55', None, ['54', '56', '62'], None),
        '56': Node('56', None, ['55'], None),
        '57': Node('57', None, ['48', '63'], None),
        '58': Node('58', None, ['50', '59', '64'], None),
        '59': Node('59', None, ['51', '58', '60', '65'], None),
        '60': Node('60', None, ['52', '59', '66'], None),
        '61': Node('61', None, ['54', '62'], None),
        '62': Node('62', None, ['55', '61'], None),
        '63': Node('63', None, ['57'], None),
        '64': Node('64', None, ['58', '65'], None),
        '65': Node('65', None, ['59', '64', '66'], None),
        '66': Node('66', None, ['60', '65', '67'], None),
        '67': Node('67', None, ['66'], None)
    }

    frontier = [initialState]
    explored = []

    while (len(frontier)!=0):
        currentNode = frontier.pop(0)
        print("Current Node: ",currentNode)

        explored.append(currentNode)
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                frontier.append(child)

solution = BFS()
print(solution)