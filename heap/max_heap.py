class Heap:
    def __init__(self):
        self.storage = []
        #parent - 1/2
        #Left - 1 * 2
        #right - i * 2 + 1 

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self._swap(1, len(self.storage) - 1)
        max_value = self.storage.pop()
        self._sift_down(0)
        return max_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage) - 1

    def _swap(self, firstIndex, secondIndex):
        temp = self.storage[firstIndex]
        self.storage[firstIndex] = self.storage[secondIndex]
        self.storage[secondIndex] = temp

    def _bubble_up(self, index):
        parentIndex = index -1 // 2 
        if index <= 1:
            return 
        elif self.storage[parentIndex] < self.storage[index]:
            self._swap(parentIndex, index)
            self._bubble_up(parentIndex)

            

    def _sift_down(self, index):
        leftChild = index * 2 + 1
        rightChild = index * 2 + 2
        max_value = index
        if len(self.storage) > leftChild and self.storage[max_value] < self.storage[leftChild]:
            max_value = leftChild
        if len(self.storage) > rightChild and self.storage[max_value] < self.storage[rightChild]:
            max_value = rightChild
        if max_value != index:
            self._swap(max_value, index)
            self._sift_down(max_value)
