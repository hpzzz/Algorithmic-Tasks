class Node(object):
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.right = None
        self.left = None
    def find(self, k):
        #Find and return the node with the key k from the subtree rooted at this node
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        #Find the node with the minimum key in the subtree rooted at this node.

        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        #Returns the node with the next largest key
        if self.right is not None:
            self.right.find_min()
        
        current = self
        #go to the most left node - its parent is next larger
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent
