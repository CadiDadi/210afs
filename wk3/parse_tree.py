
# 1. Review section "Parsing a reverse Polish expression" from book.

# 2. Create a new file called parsetree.py in your Week 3 folder

# 3. Download and import "print_tree.py  download" code into your parsetree.py
import print_tree

# 4. Create a node class to store data in a parse treer
    #  - Node should have reference links to left, right and parent 
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left  
        self.right = right
        self.parent = parent

# 5. Create a function to build a parse tree from a fully parenthesized mathematical expression in infix notation. 
    # - Example of mathematical expression: ( ( 11 * 2 ) + ( 10 - 2 ) ).
    # - You will want to break up the expression string into one of four different types of tokens (cases): left parentheses, right parentheses, operators, and operands.
def buildTree(exp):
    

# 6. Create a function to traverse and print the parse tree in order .  You will need to use recursion.
def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.val, end = " ")
        inOrder(node.right)

# 7. Create a function to traverse and print the parse tree in pre-order. You will need to use recursion.
def preOrder(node):
    if node:
        print(node.val, end = " ")
        preOrder(node.left)
        preOrder(node.right)

# 8. Create a function to traverse and print the parse tree in post-order. You will need to use recursion.
def postOrder(node):
    postOrder(node.left)
    postOrder(node.right)
    print(node.val, end = " ")

# 9. Call your function to build a parse tree from the below listed input.
buildTree("( ( 11 * 2 ) + ( 10 - 2 ) )")

# 10. Call the print_tree function to print the tree.

# 11. Call each of the three different traverse functions (in-order, pre-order, post-order) to print the tree’s contents
    # Notes:
        # Tree Traversals
            # PreOrder 
                #     - Visit root node first
                #     - Recursively do a preorder traversal of the left subtree
                #     - Recursively do a preorder traversal of the right subtree
                
            # InOrder
                #     - Recursively do a inorder traversal of the left subtree
                #     - Visit root node first
                #     - Recursively do a inorder traversal of the right subtree

            # PostOrder
                #     - Recursively do a postorder traversal of the left subtree
                #     - Recursively do a postorder traversal of the right subtree
                #     - Visit root node first        

# Input:
    #  ( ( 11 * 2 ) + ( 10 - 2 ) )

# Expected output:
    #    _+__  
    #   /    \
    #   *     -
    #  / \   / \
    # 11 2  10  2

    # Preorder:
    # + * 11 2 - 10 2
    # InOrder:
    # 11 * 2 + 10 - 2
    # Postorder:
    # 11 2 * 10 2 - +
    