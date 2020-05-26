class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []


def bfs(first_node):
    """Breadth-first search graph traversing algorithm"""
    queue = []
    queue.append(first_node)

    while queue:
        actual_node = queue.pop(0)

        actual_node.visited = True
        print(actual_node.name)

        for node in actual_node.neighbours:
            if not node.visited and node not in queue:
                queue.append(node)


def dfs(node):
    """Depth-first search graph traversing algorithm"""
    print(node.name)
    node.visited = True

    for n in node.neighbours:
        if not n.visited:
            dfs(n)


def generate_nodes():
    node_1 = Node('A')
    node_2 = Node('B')
    node_3 = Node('C')
    node_4 = Node('D')
    node_5 = Node('E')

    node_1.neighbours.append(node_2)
    node_1.neighbours.append(node_3)
    node_2.neighbours.append(node_4)
    node_2.neighbours.append(node_3)
    node_4.neighbours.append(node_5)

    return node_1


node = generate_nodes()
print('BFS')
print(bfs(node))

node = generate_nodes()
print('DFS')
print(dfs(node))
