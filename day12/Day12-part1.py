from dijkstar import Graph, find_path
from string import ascii_lowercase

letterValues = {}
i = 1
for c in ascii_lowercase:
    letterValues[c] = i
    i += 1

letterValues["S"] = 0
letterValues["E"] = i

graph = Graph()

nodes = []
f = open("Day12-input.txt")
for line in f:
    line = line.strip()
    helpList = []
    for c in line:
        helpList.append(c)
    nodes.append(helpList)

def calculateCost(node1, node2):
    if abs(node1 - node2) > 1:
        return 10000000000
    else:
        return abs(node1 - node2)

for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        if nodes[i][j] == "S":
            startPoint = f"{i}, {j}, {nodes[i][j]}"

        if nodes[i][j] == "E":
            endPoint = f"{i}, {j}, {nodes[i][j]}"
        
        # print(f"i: {i} j: {j}")
        if i == 0 and j == 0:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)

        elif i == 0 and j == len(nodes[i]) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)

        elif i == len(nodes) - 1 and j == 0:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)

        elif i == len(nodes) - 1 and j == len(nodes[i]) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)

        elif i == 0 and j > 0 and j != len(nodes[i]) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)

        elif j == 0 and i > 0 and i != len(nodes) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)

        elif i == len(nodes) - 1 and j > 0 and j != len(nodes[i]) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)

        elif j == len(nodes[i]) - 1 and i > 0 and i != len(nodes) - 1:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)

        else:
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i+1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i+1}, {j}, {nodes[i+1][j]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i-1][j]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i-1}, {j}, {nodes[i-1][j]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j-1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j-1}, {nodes[i][j-1]}", cost)
            cost = calculateCost(letterValues[nodes[i][j]], letterValues[nodes[i][j+1]])
            graph.add_edge(f"{i}, {j}, {nodes[i][j]}", f"{i}, {j+1}, {nodes[i][j+1]}", cost)




# print(nodes)
# print(graph)

result = find_path(graph, startPoint, endPoint)

print(result.nodes)
print(len(result.costs))
print(len(result.edges))
print(letterValues)

# def cost_func(u, v, edge, prev_edge):
#     length, name = edge
#     if prev_edge:
#         prev_name = prev_edge[1]
#     else:
#         prev_name = None
#     cost = length
#     if name != prev_name:
#        cost += 10
#     return cost

# PathInfo(
#     nodes=[1, 2, 3, 4],
#     edges=[(110, 'Main Street'), (125, 'Main Street'), (108, '1st Street')],
#     costs=[120, 125, 118],
#     total_cost=363)