from typing import List

from yoga.trees.insert_and_delete import BinaryTreeNode, BinarySearchTree

class Solution:
    def binaryTreePaths(self, root: BinaryTreeNode) -> List[str]:
        paths = []
        
        def dfs(root, path_str = ''):
            if root:
                path_str += str(root.val)
                if root.left:
                    left_path_str = path_str + '->'  # New local path_str is reqd for every path rooted at root
                    dfs(root.left, left_path_str)
                if root.right:
                    right_path_str = path_str + '->'
                    dfs(root.right, right_path_str)
                    
                if not root.left and not root.right: #Print when you are a leaf node
                    paths.append(path_str)
        
        dfs(root)
        return paths
    
if __name__ == '__main__':
    sol = Solution()

    myBT = BinarySearchTree()

    inputs = [19, 7, 43, 3, 11, 23, 47, 2, 5, 37, 53, 29, 41, 31]

    for input in inputs:
        myBT.insert(input)
    
    print(sol.binaryTreePaths(myBT.get_root()))