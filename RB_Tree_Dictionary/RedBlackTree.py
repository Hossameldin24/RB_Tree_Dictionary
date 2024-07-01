from Node import Node

class RB_Tree:
    def __init__(self):
        
        self.NiL = Node(None, "B")
        self.root = self.NiL

    def search(self, key):
        
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        
        if node == self.NiL or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def insert(self, key):
        
        new = Node(key)
        new.right = self.NiL
        new.left = self.NiL
        parent = None
        index = self.root
        
        while index != self.NiL:
            parent = index
            if new.key >= index.key:
                index = index.right
            else:
                index = index.left
        
        new.parent = parent
        if parent == None:
            self.root = new
        elif new.key < parent.key:
            parent.left = new
        else:
            parent.right = new
        new.color = "R"
        self.insertionFixup(new)

    def LeftRotate(self, node):
        
        y = node.right
        node.right = y.left
        if y.left != self.NiL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.NiL:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def RightRotate(self, node):
        
        y = node.left
        node.left = y.right
        if y.right != self.NiL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.NiL:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insertionFixup(self, node):
       
        while node != self.root and node.parent.color == "R":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.LeftRotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.RightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "R":
                    node.parent.color = "B"
                    uncle.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.RightRotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.LeftRotate(node.parent.parent)
        self.root.color = "B"

    def printTreeHeight(self):
        
        return self._calculateTreeHeight(self.root)

    def _calculateTreeHeight(self, node):
        
        if node == self.NiL:
            return 0
        else:
            heightL = self._calculateTreeHeight(node.left)
            heightR = self._calculateTreeHeight(node.right)
            return max(heightR, heightL) + 1

    def printBlackHeight(self):
        
        return self._calculateBlackHeight(self.root)

    def _calculateBlackHeight(self, node):
        
        if node == self.NiL:
            return 0
        left_black_height = self._calculateBlackHeight(node.left)
        right_black_height = self._calculateBlackHeight(node.right)
        if node.color == 'B':
            return max(left_black_height, right_black_height) + 1
        else:
            return max(left_black_height, right_black_height)

    def printTreeSize(self):
        
        return self._calculateTreeSize(self.root)

    def _calculateTreeSize(self, node):
        
        if node == self.NiL:
            return 0
        return self._calculateTreeSize(node.left) + self._calculateTreeSize(node.right) + 1


""" array = [8, 3, 17, 9, 6, 1, 21]
dictionary = RB_Tree()
for word in array:
    dictionary.insert(word)
    

print("Tree height:", dictionary.printTreeHeight())
print("Black height:", dictionary.printBlackHeight())
print("Tree size:", dictionary.printTreeSize())
 """