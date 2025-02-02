import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(arr):
    if not arr:
        return None

    nodes = [Node(val) for val in arr]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def generate_colors(n):
    colors = []
    for i in range(n):
        color = "#{:02x}{:02x}{:02x}".format(int((255 / n) * i), 0, 255 - int((255 / n) * i))
        colors.append(color)
    return colors

def bfs(tree_root):
    queue = deque([tree_root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def dfs(tree_root):
    stack = [tree_root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def visualize_traversal(tree_root, order):
    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
    draw_tree(tree_root)

# Приклад використання
if __name__ == "__main__":
    heap_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Створення дерева з купи
    heap_tree_root = build_heap_tree(heap_array)

    # Обхід в ширину (BFS)
    bfs_order = bfs(heap_tree_root)
    print("Обхід в ширину (BFS):")
    for node in bfs_order:
        print(node.val, end=" ")

    visualize_traversal(heap_tree_root, bfs_order)

    # Обхід в глибину (DFS)
    dfs_order = dfs(heap_tree_root)
    print("\nОбхід в глибину (DFS):")
    for node in dfs_order:
        print(node.val, end=" ")

    visualize_traversal(heap_tree_root, dfs_order)
