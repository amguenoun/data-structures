import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def traverse(node):
            if value < node.value:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = BinarySearchTree(value)
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = BinarySearchTree(value)


        traverse(self)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def find(node):
            if node is None:
                return False
            elif target == node.value:
                return True
            elif target < node.value:
                return find(node.left)
            else:
                return find(node.right)

        return find(self)

    # Return the maximum value found in the tree
    def get_max(self):
        def traverse_right(node):
            if node.right:
                return traverse_right(node.right)
            else:
                return node.value
                
        return traverse_right(self)

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def hit(node):
            if node.right:
                hit(node.right)
            if node.left:
                hit(node.left)
            cb(node.value)

        hit(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.size != 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self)
        if self.right:
            self.right.pre_order_dft(self)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self)
        if self.right:
            self.right.post_order_dft(self)
        print(self.value)
