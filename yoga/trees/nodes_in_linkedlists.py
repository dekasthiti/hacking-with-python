from yoga.trees.insert_and_delete import BinarySearchTree, BinaryTreeNode

from collections import deque
from typing import List

class LinkedListNode:
    def __init__(self, val:int=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        # Initialize an empty linkedlist
        self._head = None
        self._tail = None
        
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail
    
    def insert_last(self, new_node):
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # update the tail
            curr = self._tail
            curr.next = new_node
            self._tail = new_node
        

class BST_LL(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.linkedlist_list = []
    
    def create_linkedlist(self, curr_q:deque, linked_list: List[LinkedListNode] = []):
        
        # Do breadth-first traversal, i.e, visit the children before visiting grandchildren
        
        d_ll = LinkedList()
        
        while curr_q:
            bst_node = curr_q.popleft()
            
            if bst_node:
                ll_node = LinkedListNode(bst_node.val)
                d_ll.insert_last(ll_node)
                
        linked_list.append(d_ll.get_head())
        
    def traverse_breadth_first(self, node: BinaryTreeNode, linked_list: List[LinkedListNode] = []):
        if node:
            curr_q = deque()
            next_q = deque()
            
            curr_q.append(node)
            next_q.append(node.left)
            next_q.append(node.right)
            
            while curr_q:
                
                # This call will also empty the curr_q
                self.create_linkedlist(curr_q, linked_list)
                # update curr_q
                curr_q = next_q.copy()
                next_q.clear()
                
                # Update next_q
                for node in curr_q:
                    if node:
                        if node.left: next_q.append(node.left)
                        if node.right: next_q.append(node.right)
        
    def print_linkedlist(self, Dll_head):
        ll_node = Dll_head
        while ll_node:
            print(ll_node.val, end=',')
            ll_node = ll_node.next
            
        
# CTCI: Problem 4.4:
# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at a given depth D
if __name__ == '__main__':
    
    inputs = [19, 7, 43, 3, 11, 23, 47, 2, 5, 17, 37, 53, 13, 29, 41, 31]

    myBST_LL = BST_LL()
    # Create the tree
    for node_val in inputs:
        myBST_LL.insert(node_val)
        
    print("Tree is:")
    myBST_LL.print_tree()
    
    # Traverse the tree, create linkedlists and return
    D_linkedlists = []
    
    myBST_LL.traverse_breadth_first(myBST_LL.get_root(), D_linkedlists)
    
    if D_linkedlists:
        print("Linked Lists:")
        for D_ll in D_linkedlists:
            myBST_LL.print_linkedlist(D_ll)
            print('\n')
    