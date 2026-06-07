'''CalcIter7. Расширить класс двусвязного циклического списка с барьерным элементом из
лабораторной работы №16 интерфейсом итератора. Итератор должен возвращать все
элементы списка в прямом порядке без остановки. Вместо значения барьерного элемента
итератор должен возвращать строку «barrier».'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularListWithBarrier:
    def __init__(self):
        self.barrier = Node()
        self.barrier.prev = self.barrier
        self.barrier.next = self.barrier
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        last = self.barrier.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.barrier
        self.barrier.prev = new_node
        self._size += 1

    def prepend(self, data):
        new_node = Node(data)
        first = self.barrier.next
        self.barrier.next = new_node
        new_node.prev = self.barrier
        new_node.next = first
        first.prev = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __iter__(self):
        return CircularForwardIterator(self.barrier)


class CircularForwardIterator:
    def __init__(self, barrier_node):
        self.barrier = barrier_node
        self.current = barrier_node.next

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is self.barrier:
            self.current = self.current.next
            return "barrier"
        data = self.current.data
        self.current = self.current.next
        return data
    

lst = DoublyCircularListWithBarrier()
lst.append(10)
lst.append(20)
lst.prepend(5)


it = iter(lst)

for i in range(10):
    print(next(it))