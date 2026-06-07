'''TreeFun1. Преобразовать бинарное дерево поиска в двусвязный список без использования
дополнительной памяти (создания новых объектов). При преобразовании поля left и right
узлов бинарного дерева рассматриваются эквивалентными полям prev и next узлов
двусвязного списка. Вывести исходное дерево и получившийся список. Элементы в
результирующем списке должны сохранить свою упорядоченность.'''



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_print(root):
    if root is None:
        return
    inorder_print(root.left)
    print(root.val, end=' ')
    inorder_print(root.right)

def convert_to_list(root):
    if root is None:
        return (None, None)
    left_head, left_tail = convert_to_list(root.left)
    right_head, right_tail = convert_to_list(root.right)

    if left_tail:
        left_tail.right = root
        root.left = left_tail
    if right_head:
        right_head.left = root
        root.right = right_head

    head = left_head if left_head else root
    tail = right_tail if right_tail else root
    return (head, tail)

def print_list(head):
    print("Прямой порядок:", end=' ')
    cur = head
    while cur:
        print(cur.val, end=' ')
        if cur.right is None:
            tail = cur
        cur = cur.right
    print()
    print("Обратный порядок:", end=' ')
    cur = tail
    while cur:
        print(cur.val, end=' ')
        cur = cur.left
    print()

if __name__ == "__main__":
    #                      5
    #                    /   \
    #                   3     7
    #                  / \   / \
    #                 2   4 6   8
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    inorder_print(root)
    print()

    head, tail = convert_to_list(root)
    print("Полученный двусвязный список:")
    print_list(head)