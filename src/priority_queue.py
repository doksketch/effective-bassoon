from math import floor

class PriorityHeap:

    def __init__(self):
        self.heap = []

    # методы адресации к стеку
    def get_parent_position(self, i):
        return floor((i - 1) / 2)

    def get_left_child_position(self, i):
        return 2 * i + 1

    def get_right_child_position(self, i):
        return 2 * i + 2

    # методы проверки того, есть ли в узлах ответвления
    def has_parent(self, i):
        return self.get_parent_position(i) < len(self.heap)

    def has_left_child(self, i):
        return self.get_left_child_position(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child_position(i) < len(self.heap)

    # вставка элемента в стэк
    def insert(self, item):
        self.heap.append(item)
        self.heapify(len(self.heap) - 1) # перестроение стэка с сохранением его свойств

    def heapify(self, i):
        # двигаемся до тех пор, пока не достигнем листа
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent_position(i)]:
            self.heap[i], self.heap[self.get_parent_position(i)] = self.heap[self.get_parent_position(i)], \
                                                                   self.heap[i]  # меняем местами элементы
            i = self.get_parent_position(i) # обновляем позицию в массиве

    def get_max_item(self, k):
        return self.heap[k]