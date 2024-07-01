class Node:
    def __init__(self, key, color="R"):
        
        self.color = color
        self.key = key
        self.right = None
        self.left = None
        self.parent = None