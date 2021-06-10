from typing import List

class BinaryTreeNode:
    def __init__(self, val:int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def get_root(self):
        return self._root
        
    def insert(self, key: int):
        # 1. If tree is empty, create a node and set the root to this node
        if self._root is None:
            self._root = BinaryTreeNode(key)
            
        
        # 2. Search for a place to insert
        # Specifically, search for the parent whose child can be this node
        # If node is already in the tree, return because duplicates are not allowed
        # Start from the root, root's parent is None
        parent = None
        curr = self._root
        
        while curr:
            # Save the parent because curr will be updated in this step
            parent = curr
            
            if key is None:
                return
                
            if curr.val == key:
                return False
                
            elif key < curr.val:
                # else, Search left subtree
                curr = curr.left
                
            else:
                # Search the right subtree
                curr = curr.right
                
        # Found a parent whose left or right subtree is null
        if key < parent.val:
            parent.left = BinaryTreeNode(key)
        else:
            parent.right = BinaryTreeNode(key)
            
        return True
    
    def delete(self, key):
        # Search the key
        curr = self._root
        parent = None
        
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        # If we broke out of while because we couldn't find the node and reached the end of BST
        if not curr:
            return False
        
        # Found the node, it's the curr node, will have to delete it.
        # Check if it has a right subtree. If it does, it will be replaced by the leftmost node of the right subtree
        # Save the curr
        node_to_delete = curr
        if curr.right:
            r_curr = curr.right
            r_curr_parent = curr
            
            while r_curr.left:
                r_curr_parent = r_curr
                r_curr = r_curr.left
            
            # Reached the end of the left subtree of the right child
            # Update the node_to_delete's value. So instead of deleting this node, we update it's value to the
            # leftmost node of the right subtree (its inorder successor)
            node_to_delete.val = r_curr.val
            
            # Now delete the inorder successor from the tree
            # If inorder successor has right subtree (it doesn't have left subtree since it is the leftmost node
            if r_curr_parent.left == r_curr:
                r_curr_parent.left = r_curr.right
            else:
                # This case is in the book. Don't know how the leftmost node will have a left subtree
                r_curr_parent.right = r_curr.right
                
        else:
            
            # If it doesn't have a right subtree, then it's left subtree become parent's left subtree
            if self._root == node_to_delete:
                self._root = node_to_delete.left
            else:
                # node_to_delete has no right subtree, and is right child of parent
                if parent.right == node_to_delete:
                    parent.right = node_to_delete.left
                else:
                    # node_to_delete has no right subtree and is the left child of the parent
                    parent.left = node_to_delete.left
    
    def inorder_traversal(self, node: BinaryTreeNode, traversed_list: List=[]):
        if node:

            self.inorder_traversal(node.left, traversed_list)
            traversed_list.append(node.val)
            self.inorder_traversal(node.right, traversed_list)
            return
        
    def preorder_traversal(self, node: BinaryTreeNode, traversed_list: List=[]):
        if node:
            traversed_list.append(node.val)
            self.preorder_traversal(node.left, traversed_list)
            self.preorder_traversal(node.right, traversed_list)
            return
        
    def postorder_traversal(self, node: BinaryTreeNode, traversed_list: List=[]):
        if node:
            self.postorder_traversal(node.left, traversed_list)
            self.postorder_traversal(node.right, traversed_list)
            traversed_list.append(node.val)
            return
        
    def print_tree(self):
        node = self.get_root()
        traversed_list = []
        self.inorder_traversal(node, traversed_list)
        print(traversed_list)
                    
if __name__ == '__main__':
    myBT = BinarySearchTree()
    
    inputs = [19, 7, 43, 3, 11, 23, 47, 2, 5, 37, 53, 29, 41, 31]
    
    # Create the BST by inserting
    for input in inputs:
        myBT.insert(input)
    
    # Traverse the BST
    
    print("Inorder traversal: ")
    result = []
    myBT.inorder_traversal(myBT.get_root(), result)
    print(result)
    
    print("\nPre-order traversal: ")
    result = []
    myBT.preorder_traversal(myBT.get_root(), result)
    print(result)
    
    print("\nPost-order traversal: ")
    result=[]
    myBT.postorder_traversal(myBT.get_root(), result)
    print(result)
    