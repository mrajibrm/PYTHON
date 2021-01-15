
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def createNode(val): #function that allocates a new node with the given data and None left and right pointers
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None
    return newNode


def inorder(root): #  function to print Inorder traversal
    if (root == None):
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# mirrorify function takes two trees, original tree and a mirror tree
# It recurses on both the trees,but when original tree recurses on left, mirror tree recurses on right and vice-versa
def mirrorify(root, mirror):

    if (root == None):
        mirror = None
        return mirror
    mirror = createNode(root.val)   # Create new mirror node from original tree node
    mirror.right = mirrorify(root.left,
                             ((mirror).right))
    mirror.left = mirrorify(root.right,
                            ((mirror).left))
    return mirror


# Driver Code
if __name__ == '__main__':

    tree = createNode(1)
    tree.left = createNode(2)
    tree.right = createNode(3)
    tree.left.right = createNode(4)
    tree.right.left = createNode(5)
    tree.right.right = createNode(6)
    tree.right.left.right = createNode(7)
    
    print("Inorder of original tree: ")# Print inorder traversal of the input tree
    inorder(tree)
    mirror = None
    mirror = mirrorify(tree, mirror)

    print("\nInorder of mirror tree: ") # Print inorder traversal of the mirror tree
    print(inorder(mirror))
    # print(type(mirror))
 
