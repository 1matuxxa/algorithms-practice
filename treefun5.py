'''TreeFun5. Реализовать для бинарного дерева интерфейс итератора, который будет возвращать
значения элементов, находящихся в узлах дерева, в порядке "лево-право-корень".
Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать
запрещается.'''



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class PostOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.last_visited = None
        self._push_left_path(root)

    def _push_left_path(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.right is None or self.last_visited == cur.right:
                self.stack.pop()
                self.last_visited = cur
                return cur.val
            self._push_left_path(cur.right)
        raise StopIteration

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

    it = PostOrderIterator(root)
    for val in it:
        print(val, end=' ')
    print()