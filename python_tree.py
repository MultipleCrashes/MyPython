

class Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 


class TreeApp:

    def __init__(self):
        self.root_node = None 

    def add_node(self, data):
        new_node = Tree(data)
        if self.root_node == None:
            self.root_node = new_node  
        else:
            current = self.root_node
            while(current!=None):
                if data > current.data:
                    current = current.right
                else:
                    current = current.left 
            current = new_node

    def traverse_tree(self):
        if self:
            print(self.root_node.data)
            self.traverse_tree(self.left)
            self.traverse_tree(self.right)




if __name__ == '__main__':
    tree_obj = TreeApp()
    tree_obj.add_node(10)
    tree_obj.add_node(20)
    tree_obj.add_node(30)
    tree_obj.traverse_tree()
                
            
