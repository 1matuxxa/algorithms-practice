'''SimpleIter1. Написать класс, реализующий интерфейс итератора. Класс должен принимать в
конструкторе список элементов произвольного типа и позволять просмотреть его в обратном
порядке'''

class ReverseListIterator:
    def __init__(self, items):
        self._items = items
        self._index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        value = self._items[self._index]
        self._index -= 1
        return value

list = [10,30,40,12000]
list_rev = ReverseListIterator(list)

for i in list_rev:
    print(i)
    