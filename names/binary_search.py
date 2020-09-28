# Creating a BSTNode Class here, as we are going to need to utilize a Binary Search in order to improve the Runtime of names.py

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        if value < self.value:
           if self.left is None:
            self.left = BSTNode(value)
           else:
            self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)