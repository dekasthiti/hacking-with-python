from typing import List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def remove(self):
        self.left = self.right = None
        del self

class Solution:
    def __init__(self):
        self.forest = []
        self.trees = defaultdict(list)
    
    def build_tree(self, root):
        tree = []
        for entry in root:
            node = TreeNode(val = entry)
            tree.append(node)
            
        # Update root
        self.root = tree[0]
        # self.forest.append(self.root)

        # Now make the connections
        q = deque()
        # for tree_idx, tree_node in enumerate(tree):
        list_idx = tree_idx = 0
    
        #q.append(tree_node)
        q.append(tree[0])

        #Q pop keeps track of the parents, list_idx keeps track of the children
        while q:
            print([node.val for node in q])
            node = q.popleft()
            print(f"Popped {node.val}")
            if node and (list_idx + 1) < len(tree):
                node.left = tree[list_idx + 1]
                list_idx += 1
                q.append(node.left)
    
                if (list_idx + 1) < len(tree):
                    node.right = tree[list_idx + 1]
                    list_idx += 1
                    q.append(node.right)
                else:
                    node.right = None
            else:
                node.left = None
                break
                    
        return self.root

    def remove(self, node_to_del):
        root = self.root
        
        q = deque()
        
        q.append(root)
        while q:
            curr_node = q.popleft()
            
            if not curr_node:
                return
            # Found the node to delete
            #if curr_node.val == node.val:  # This is a bug! What is node??
            if curr_node == node_to_del: # This should be the right check
                curr_node.left = curr_node.right = None
                curr_node = None
                del curr_node
                break
            # Haven't found the node to delete yet, look to the left and right children
            else:
                q.append(curr_node.left)
                q.append(curr_node.right)
                
    def remove2(self, root, node_to_del):
        q = deque()
        q.append(root)
        while(q):
            node = q.popleft()
            
            # This doesn't work. Deleting a pointer that is referenced doesn't work
            # if node.val == node_to_del:
            #     if node.left: node.left = None
            #     if node.right: node.right = None
            #     node.val = 0
            #     del node
            #     break
            # else:
            #     if node.left: q.append(node.left)
            #     if node.right: q.append(node.right)
            if node.left and node.left.val == node_to_del:
                node.left = None
                break

            elif node.right and node.right.val == node_to_del:
                node.right = None
                break
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
            
        del q
        return
                
    def traverse_tree(self, root, nodes_list:List = []):
        if not root:
            return 'null'
        nodes_list.append(root)
        self.traverse_tree(root.left, nodes_list)
        self.traverse_tree(root.right, nodes_list)
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # 1. Base case: Empty tree
        if not root:
            return []
        else:
            q = deque()
            q.append(root)
            
            while q:
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right or None)
                if root.val in to_delete:
                    print(f"\n{root.val} in to_delete list")
                    if root in self.forest:
                        print(f"Removing {root.val} from forest")
                        
                        self.forest.remove(root)
                    self.forest.append(root.left) if root.left else None
                    
                    if root.left:
                        print(f"Adding {root.left.val} to forest")
                        
                    self.forest.append(root.right) if root.right else None
                    
                    if root.right:
                        print(f"Adding {root.right.val} to forest")
                    
                    # Remove the root from the original tree root
                    #self.remove(root)
        
                    # Remove the children from the original tree root
                    # self.remove(root.left)
                    # self.remove(root.right)

                else:
                    if root == self.root:
                        self.forest.append(self.root)
                        
        for node in self.forest:
            for del_node in to_delete:
                self.remove2(node, del_node)
        # self.delNodes(root.left, to_delete)
        # self.delNodes(root.right, to_delete)
        
        
        # idx = 0
        # while idx < len(self.forest):
        #     node = self.forest[idx]
        #     if node.val in to_delete:
        #         self.forest.remove(node)
        #         self.forest.append(node.left)
        #         self.forest.append(node.right)
        #         del node
        #     else:
        #         self.delNodes(node.left, to_delete)
        #         self.delNodes(node.right, to_delete)

            
            
            
            
            
            
            # while root:
            #     q.append(root)
            #     while q:
            #         node = q.pop()
            #         if node and node.val in to_delete:
            #             q.append(node.left)
            #             q.append(node.right)
            #
            #             tree_roots.append(node.left)
            #             tree_roots.append(node.right)
            #
            #             # Delete the node
            #             node.left = node.right = None
            #             del node
            #
            #     if root.left:
            #         root = root.left
            #     elif root.right:
            #         root = root.right
            #     else:
            #         root = None
            #
            # forest = []
            # # Traverse the tree roots in tree_roots
            # for idx, tree_root in enumerate(tree_roots):
            #     # expanded_tree = self.traverse_tree(tree_root)
            #     #forest.append(expanded_tree)
            #     forest.append(tree_root)
        
        return self.forest
    
if __name__ == '__main__':
    sol = Solution()
    root = [1, 2, 3, 4, 5, 6, 7]
    to_delete = [ 3, 5,]
    
    tree_root = sol.build_tree(root)
    traversed_list = []
    sol.traverse_tree(tree_root, traversed_list)
    print("Tree is")
    for node in traversed_list:
        print(node.val, end=' ')
    forest = sol.delNodes(tree_root, to_delete)
    
    expanded_forest = []
    print(f"Forest is: {[root_node.val for root_node in forest]}")
    for root_node in forest:
        # print(root_node.val, end=',')
        nodes_list = []
        sol.traverse_tree(root_node, nodes_list)
        for node in nodes_list:
            print(node.val, end=',')
        print("\n")
        expanded_forest.append(nodes_list)
        
    print([[node.val for node in roots] for roots in expanded_forest])
