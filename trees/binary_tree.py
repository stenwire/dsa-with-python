class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        new_node = Tree(value)
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)
                
    # L - N - R
    def inorder_tr(self):
        if self.left:
            self.left.inorder_tr()
        print(self.value)
        if self.right:
            self.right.inorder_tr()
            
    # N - L - R
    def preorder_tr(self):
        print(self.value)
        if self.left:
            self.left.preorder_tr()
        if self.right:
            self.right.preorder_tr()

    # L - R - N        
    def postorder_tr(self):
        if self.left:
            self.left.postorder_tr()
        if self.right:
            self.right.postorder_tr()
        print(self.value)
        
    
    def find(self, value):
        if value < self.value:
            # move to left hand side
            if self.left:
                return self.left.find(value)
            return False
        elif value > self.value:
            # move to right hand side
            if self.right:
                return self.right.find(value)
            return False
        else:
            print(f"{self.value} == {value}")
            return True

            
            
def operation():
    new_tree = Tree(67)
    new_tree.insert(32)
    new_tree.insert(23)
    new_tree.insert(12)
    new_tree.insert(54)
    new_tree.insert(90)
    new_tree.insert(2)
    new_tree.insert(74)
    new_tree.insert(10)
    return new_tree

def main():
    op = operation()
    print("==== In Order ======")
    op.inorder_tr()
    print("==== Pre Order ======")
    op.preorder_tr()
    print("==== Post Order ======")
    op.postorder_tr()
    print("==== Find value ======")
    print(op.find(10))
    

main()
