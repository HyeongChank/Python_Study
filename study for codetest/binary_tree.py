class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(int(input("Enter root value: ")))

num_inserts = int(input("Enter number of elements to insert: "))
for _ in range(num_inserts):
    value = int(input("Enter a number to insert: "))
    insert(r, Node(value))

print("Inorder traversal of the BST:")
inorder(r)
