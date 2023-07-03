# class Node:
#     def __init__(self,key):
#         self.left = None
#         self.right = None
#         self.val = key
 
# def insert(root,node):
#     if root is None:
#         root = node
#     else:
#         if root.val < node.val:
#             if root.right is None:
#                 root.right = node
#             else:
#                 insert(root.right, node)
#         else:
#             if root.left is None:
#                 root.left = node
#             else:
#                 insert(root.left, node)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)

# r = Node(int(input("Enter root value: ")))

# num_inserts = int(input("Enter number of elements to insert: "))
# for _ in range(num_inserts):
#     value = int(input("Enter a number to insert: "))
#     insert(r, Node(value))

# print("Inorder traversal of the BST:")
# inorder(r)











# class Node:
#     def __init__(self, key):
#         self.right = None
#         self.left = None
#         self.key = key
        
# def insert(root, node):
#     if root is None:
#         root = node
#     else:
#         if root.key < node.key:
#             if root.right is None:
#                 root.right = node
#             else:
#                 insert(root.right, node)
#         else:
#             if root.left is None:
#                 root.left = node
#             else:
#                 insert(root.left, node)
                
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.key)
#         inorder(root.right)
        
        
# r = Node(int(input("root")))
# num = int(input("num"))

# for i in range(num):
#     add = int(input("add"))
#     insert(r, Node(add))
    
# inorder(r)









class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.key < node.key:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.key >= node.key:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def find(root, key):
    # return 을 써야 반복해서 출력되지 않음
    def operate(root, key):
        if root:
            if root.key == key:
                return 1
            elif root.key < key:
                return operate(root.right, key)
            elif root.key > key:
                return operate(root.left, key)
        return 0
    
    if operate(root, key) ==1:
        print("exist")
    else:
        print("not exist")
        
                
def inorder(r):
    if r:
        inorder(r.left)
        print(r.key)
        inorder(r.right)

# def delete(root, key):
#     if root:
#         if root.key == key:
# def minValueNode(node):
#     current = node
#     while(current.left is not None):
#         current = current.left
#     return current

# def deleteNode(root, key):
#     if root is None:
#         return root

#     # If the key to be deleted is smaller than the root's key
#     if key < root.key:
#         root.left = deleteNode(root.left, key)
#     # If the key to be deleted is greater than the root's key
#     elif(key > root.key):
#         root.right = deleteNode(root.right, key)
#     # If the key is same as root's key
#     else:
#         # Node with only one child or no child
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         # Node with two children
#         # Get the inorder successor (smallest in the right subtree)
#         temp = minValueNode(root.right)
#         # Copy the inorder successor's content to this node
#         root.key = temp.key
#         # Delete the inorder successor
#         root.right = deleteNode(root.right, temp.key)
#     return root            

r = Node(int(input("root")))


print(r.key)
while True:
    x = input("select service a:find b:add c:inorder")
    match x:
        case 'a':
            find(r, int(input("find")))
        case 'b':
            insert(r, Node(int(input("add"))))
        case 'c':
            inorder(r)
            
            
            
            
            
            
            
            
            
            
    while True:
        x = input("input")
        match x:
            case 'a' :
                pass
            case 'b' :
                pass
            