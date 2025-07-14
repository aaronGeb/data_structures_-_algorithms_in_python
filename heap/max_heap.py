#!/usr/bin/env python3
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self._heapify_up(parent_index)

    def extract_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(35)
    max_heap.insert(33)
    max_heap.insert(42)
    max_heap.insert(10)
    max_heap.insert(14)
    max_heap.insert(19)
    max_heap.insert(27)
    max_heap.insert(44)
    max_heap.insert(26)
    max_heap.insert(31)
   # max_heap.print_max_heap()
    max_value = max_heap.extract_max()
    print("Maximum element:", max_value)
    print(max_heap.extract_max())  # Output: 20
    print(max_heap.extract_max())  # Output: 10
    print(max_heap.extract_max())  # Output: 5
    print(max_heap.extract_max())  # Output: None (heap is empty)
    print(max_heap.extract_max())  # Output: None (heap is empty)
