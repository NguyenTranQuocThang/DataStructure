from platform import node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value

    def set_left(self,node):
        self.left = node
    
    def set_right(self,node):
        self.right = node

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
class Tree:
    def __init__(self,value):
        self.root = Node(value)
    def get_root(self):
        return self.root
