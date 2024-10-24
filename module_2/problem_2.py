### Problem 2

class MaxHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H)-1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i//2],  f'Maxheap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'

    def max_element(self):
        return self.H[1]

    def bubble_up(self, index):
        # your code here
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] <= self.H[index]:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index] # swap
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        # your code here
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        if lchild_index >= len(self.H):
            return  # No children, so nothing to bubble down

        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else 0
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else 0
        # If the value at the index is less than or equal to the minimum of two children, then nothing else to do
        if self.H[index] >= max(lchild_value, rchild_value):
            return
        # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare
        max_child_value, max_child_index = max((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the most of its two children
        self.H[index], self.H[max_child_index] = self.H[max_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(index)

    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        self.bubble_up(self.size())

    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        if self.size() == 0:
            return
        if self.size() == 1:
            self.H.pop()  # Handle the case where there is only one element
            return
        # Swap the first element (max) with the last one and then remove the last element
        self.H[1] = self.H.pop()  # Pop the last element and put it at the root
        if self.size() > 0:
            self.bubble_down(1)  # Bubble down from the root


if __name__ == '__main__':
    h = MaxHeap()

    print('Inserting: 5, 2, 4, -1 and 7 in that order.')
    h.insert(5)
    print(f'\t Heap = {h}')
    assert(h.max_element() == 5)
    h.insert(2)
    print(f'\t Heap = {h}')
    assert(h.max_element() == 5)
    h.insert(4)
    print(f'\t Heap = {h}')
    assert(h.max_element() == 5)
    h.insert(-1)
    print(f'\t Heap = {h}')
    assert(h.max_element() == 5)
    h.insert(7)
    print(f'\t Heap = {h}')
    assert(h.max_element() == 7)
    h.satisfies_assertions()

    print('Deleting maximum element')
    h.delete_max()
    print(f'\t Heap = {h}')
    assert(h.max_element() == 5)
    h.delete_max()
    print(f'\t Heap = {h}')
    assert(h.max_element() == 4)
    h.delete_max()
    print(f'\t Heap = {h}')
    assert(h.max_element() == 2)
    h.delete_max()
    print(f'\t Heap = {h}')
    assert(h.max_element() == -1)
    # Test delete_max on heap of size 1, should result in empty heap.
    h.delete_max()
    print(f'\t Heap = {h}')

    print('All tests of MaxHeap passed!')
