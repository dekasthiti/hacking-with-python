from yoga.trees import BinaryTreeNode
from yoga.trees import BinarySearchTree

class Solution:
    def rangeSumBST(self, root: BinaryTreeNode, L: int, R: int) -> int:
        # Inorder traversal will give us the sorted array
        sorted_array = []
        def inorder_traversal(root, sorted_array):
            if not root:
                return
            else:
                inorder_traversal(root.left, sorted_array)
                sorted_array.append(root.val)
                inorder_traversal(root.right, sorted_array)
                return
        inorder_traversal(root, sorted_array)
        # print(sorted_array)
        # print(f"Index of {L}: {sorted_array.index(L)}")
        # print(f"Index of {R}: {sorted_array.index(R)}")
        return sum(sorted_array[sorted_array.index(L): sorted_array.index(R)+1])


# Leetcode: 938. Range Sum of BST
if __name__ == '__main__':
    sol = Solution()
    myBST = BinarySearchTree()
    
    inputs = [10,5,15,3,7,13,18,1,None,6]
    L=6
    R=10
    
    for input in inputs:
        myBST.insert(input)
    
    print(f"Range Sum is: {sol.rangeSumBST(myBST.get_root(), L, R)}")