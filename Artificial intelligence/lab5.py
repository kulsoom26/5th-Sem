def iterative_deepening_dfs(start, target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(start, target, 0 , depth)
        if result is not None:
            return result
        depth *= 2 
        print("Increasing depth to "+ str(depth))
    return None

def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node "+str(node["value"]))
    if node["value"] == target:
        print("Found the node we're looking for!")
        return node, True
    
    if current_depth == max_depth:
        print("Current maximum depth reached, returning....")
        if len(node["children"]) > 0:
            return None, False
        else:
            return None, True
        
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1, max_depth)
        if result is not None:
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec
        
    return None, bottom_reached

start = {
    "value": 15, "children": [{"value": 14, "children": [{"value": 13, "children": [{"value": 12, "children": [
        {"value": 11, "children": [{"value": 10, "children": [
            {"value": 9, "children": [{"value": 6, "children": []}]}, {"value": 7, "children": [{"value": 6, "children": [
                {"value": 5, "children": [{"value": 4, "children": [{"value": 8, "children": []}, {"value": 3, "children": [
                    {"value": 2, "children": [{"value": 1, "children": [{"value": 26, "children": []}, {"value": 25, "children": [
                        {"value": 24, "children": [{"value": 23, "children": [{"value": 22, "children": [{"value": 21, "children": [
                            {"value": 20, "children": [{"value": 19, "children": [{"value": 18, "children": [{"value": 17, "children": [
                                {"value": 16, "children": [{"value": 12, "children": []}]}
                            ]}]}]}]}
                        ]}]}]}]}
                    ]}]}]}
                ]}]}]}
            ]}]}
        ]}]}
    ]}]}]}]
}

print(iterative_deepening_dfs(start, 26))