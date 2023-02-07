#Task1 D
#Create a class that implements a binary search tree and can perform basic operations such as 
# insertion, deletion, and searching.

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self, value):
        self.root = self
        self.left = None
        self.right = None 
        self.value = value
        

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def search(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.search(value)
        else:
            return True

def remove(root, value):
    root = remove_node(root, value)
    return root

def remove_node(current, value):
    if current == None:
        return None
    if value < current.value:
        current.left = remove_node(current.left, value)
    elif value > current.value:
        current.right = remove_node(current.right, value)
    else:
        if current.left == None and current.right == None:
            return None
        elif current.left == None:
            return current.right
        elif current.right == None:
            return current.left
        else:
            min_node = current.right
            while min_node.left != None:
                min_node = min_node.left
            current.value = min_node.value
            current.right = remove_node(current.right, min_node.value)
    return current





#Test

tree = BinarySearchTree(10)
tree.insert(4)
tree.insert(12)
tree.insert(13)
tree.insert(5)
tree.insert(15)
print(tree.right.value)
print(tree.right.right.value)
print(tree.search(10))
print(tree.search(12))
tree = remove(tree, 10)
print(tree.search(10))
print(tree.search(12))



#Task 2
#Create a class that implements a red black tree and can perform basic operations such as 
# insertion, deletion, and searching.
import random


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left 
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right 
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num-1))
    return nums



#random test 1
tree = RBTree()
for i in range(10):
    tree.insert(random.randint(1, 100))
print(tree)


#Task 3 D
#Write a function that implements a merge sort algorithm.


def merge_sort(data):

    if len(data) <= 1:
        return data


    mid = len(data)//2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left, right):

    sorted = []
    i = 0 
    k = 0

    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[k])
            k += 1

    sorted += left[i:] + right[k:]

    return sorted


data = [3,4,2,1,6,7,5]
print(merge_sort(data))




#Task 4 D
#Write a function that implements an insertion sort algorithm.

def insertion_sort(data):
    for i in range(1, len(data)):
        while data[i-1] > data[i] and i>0:
            data [i-1], data[i] = data[i], data[i-1]
            i-=1
    print(data)

data = [3,4,2,1,6,7,5]
insertion_sort(data)


#Task 5 D
#Write a function that implements a sorting algorithm in linear time.



def counting_sort(data):

    max = 0
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]

    k = max + 1
    counts = [0] * k

    for i in range(len(data)):
        counts[data[i]] += 1


    sorted = []
    for i in range(k):
        for j in range(counts[i]):
            sorted.append(i)
    return sorted



data = [3,4,2,1,6,7,5]
print(counting_sort(data))

