class Node:
    def __init__(self, key: int, parent: "Node"=None, left: "Node"=None, right: "Node"=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

        if left:
            self.left.parent = self
        
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)

class InOrderIterator:
    def __init__(self, root: Node):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current
        
        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration
        

def traverse_in_order(root: Node):
    def in_order(current: Node):
        if current.left:
            for left in in_order(current.left):
                yield left
        yield current
        if current.right:
            for right in in_order(current.right):
                yield right
    
    for node in in_order(root):
        yield node
    

if __name__ == "__main__":
    """
        1
       / \
      2   3
    
    in-order: 213
    pre-order: 123
    post-order: 231
    """
    
    root = Node(1, left=Node(2), right=Node(3))

    it = iter(root)
    print([next(it).key for _ in range(3)])

    for node in root:
        print(node.key)

    for node in traverse_in_order(root):
        print(node.key)
