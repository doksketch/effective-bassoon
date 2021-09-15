class PriorityHeap:

    def __init__(self):
        self.heap = []

    # методы адресации к стеку
    def get_parent_position(self, node_id):
        return node_id // 2

    def get_left_child_position(self, node_id):
        child_id = 2 * node_id + 1

        if child_id < len(self.heap):
            return child_id

    def get_right_child_position(self, node_id):
        child_id = 2 * node_id + 2

        if child_id < len(self.heap):
            return child_id

    # вставка элемента в стэк
    def push(self, item):
        self.heap.append(item)
        self._go_up(len(self.heap) - 1)  # перестроение стэка с сохранением его свойств

    # взятие элемента из стэка
    def pop(self):
        if len(self.heap) > 0:
            result = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]

            self._go_down(0)

            return result

    # поднимаем элемент вверх по куче, пока не будет восстановлен порядок
    def _go_up(self, i):
        parent = self.get_parent_position(i)

        while self.heap[parent] < self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.get_parent_position(i)

    # опускаем элемент вниз по куче, пока не будет восставновлен порядок
    def _go_down(self, item):
        left_child = self.get_left_child_position(item)
        right_child = self.get_right_child_position(item)

        max_child = left_child
        if left_child:
            if right_child:
                if self.heap[right_child] > self.heap[left_child]:
                    max_child = right_child

        if max_child and self.heap[max_child] > item:
            self.heap[item], self.heap[max_child] = self.heap[max_child], self.heap[item]
            self._go_down(max_child)

    def get_top_k(self, k):
        return [self.pop() for _ in range(k)]
