'''TreeFun10. Ученые изучают поведение птиц, вьющих гнезда на бинарном дереве, и хотят
разместить в его узлах камеры. Каждая камера может обозревать узел, в котором она
расположена, а также непосредственного предка и непосредственных потомков этого узла. По
заданному бинарному дереву требуется определить, какое количество узлов будет покрыто
более чем одной камерой при самом оптимальном их размещении'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def collect_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        nodes.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return nodes

def build_parent_map(root):
    parent = {root: None}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    return parent

def is_covered(node, cameras, parent_map):
    if node in cameras:
        return True
    if parent_map[node] in cameras:
        return True
    if (node.left in cameras) or (node.right in cameras):
        return True
    return False

def count_double_covered(nodes, cameras, parent_map):
    double = 0
    for node in nodes:
        cnt = 0
        if node in cameras:
            cnt += 1
        if parent_map[node] in cameras:
            cnt += 1
        if node.left in cameras:
            cnt += 1
        if node.right in cameras:
            cnt += 1
        if cnt >= 2:
            double += 1
    return double

def find_optimal_cameras(root):
    nodes = collect_nodes(root)
    parent = build_parent_map(root)
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    min_cameras = float('inf')
    best_double = float('inf')

    for mask in range(1 << n):
        cameras = set()
        for i in range(n):
            if mask >> i & 1:
                cameras.add(nodes[i])
        all_covered = True
        for node in nodes:
            if not is_covered(node, cameras, parent):
                all_covered = False
                break
        if not all_covered:
            continue
        num_cam = len(cameras)
        if num_cam < min_cameras:
            min_cameras = num_cam
            best_double = count_double_covered(nodes, cameras, parent)
        elif num_cam == min_cameras:
            dbl = count_double_covered(nodes, cameras, parent)
            if dbl < best_double:
                best_double = dbl
    return min_cameras, best_double

if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    min_cam, double_count = find_optimal_cameras(root)
    print(min_cam)
    print(double_count)