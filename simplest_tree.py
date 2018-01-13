
class Node:

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None



def traverse(root):
    if root:
        traverse(root.left)
        print (root.data), 
        traverse(root.right)

if __name__== '__main__':
    obj = Node(5)
    obj.left = Node(10)
    obj.right = Node(20)
    obj.left.left = Node(30)
    traverse(obj)
