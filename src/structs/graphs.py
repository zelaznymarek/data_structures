class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []


class BFS:
    """Breadth-first search implementation"""

    def bfs(self, first_node):
        queue = []
        queue.append(first_node)

        while queue:
            actual_node = queue.pop(0)

            actual_node.visited = True
            print(actual_node.name)

            for node in actual_node.neighbours:
                if not node.visited and node not in queue:
                    queue.append(node)


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

bfs = BFS()
bfs.bfs(node_1)
