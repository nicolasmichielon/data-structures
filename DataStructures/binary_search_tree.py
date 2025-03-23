class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    
    if root.value == key:
        return root
    
    if root.value < key:
        root.right = insert(root.right, key)

    else:
        root.left = insert(root.left, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

r = Node(15)
r = insert(r, 10)
r = insert(r, 20)
r = insert(r, 8)
r = insert(r, 12)
inorder(r)

#How to search a value 'v' in a binary search tree?
#- Start from the root node.
#- If the root node is None, return the value.
#- If the root node's value is equal to 'v', return the value.
#- If the root node's value is less than 'v', search the right subtree.
#- If the root node's value is greater than 'v', search the left subtree.
def search(root, v):
    if root is None or root.value == v:
        return root
    
    if root.value < v:
        return search(root.right, v)
    
    return search(root.left, v)

print("Found" if search(r, 12) else "Not Found")
print("Found" if search(r, 20) else "Not Found")

#How to delete a value 'v' from a binary search tree?
#- Start from the root node.
#- If the root node is None, return the value.
#- If the root node's value is equal to 'v', delete the node.
#- If the root node's value is less than 'v', traverse through the right subtree.
#- If the root node's value is greater than 'v', traverse through the left subtree.

#CASE 1: While deleting a node having both left child and right child
## After finding the node to be deleted, copy the value of the right child to 'v' and copy the right child's left pointer to left of 'v' and right pointer.

#CASE 2: While deleting a node having only one child
## After finding the node to be deleted, we need to replace the value in the node with its left node if it has left child or right node if it has right child.

#CASE 3: While deleting a node having no child (leaf node)
## Simply we change value of the node, left and right pointers to None.

def get_successor(current):
    current = current.right
    while current is not None and current.left is not None:
        current = current.left
    return current

#This function deletes a given key 'x' from the given BST and returns the modified root of the BST.
def delete_node(root, x):
    if root is None:
        return root
    
    if root.value > x:
        root.value = delete_node(root.left, x)

    elif root.value < x:
        root.value = delete_node(root.right, x)

    else:
        #If root matches with the given key
        #Cases when root has 0 children or only right child
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        sucessor = get_successor(root)
        root.value = sucessor.value
        root.right = delete_node(root.right, sucessor.value)

    return root