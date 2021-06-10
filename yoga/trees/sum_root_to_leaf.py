from yoga.trees import BinaryTreeNode
from yoga.trees import BinarySearchTree

class Solution:
    def sumNumbers(self, root: BinaryTreeNode) -> int:
        my_list = []
        my_str = ''
    
        def traverse(root, my_str, my_list):
            if not root:
                return
            else:
                my_str += str(root.val)
                traverse(root.left, my_str, my_list)
                traverse(root.right, my_str, my_list)
                if not root.left and not root.right:
                    my_list.append(my_str)
            
                print(my_list)
                return
    
        traverse(root, my_str, my_list)
        return sum([int(item) for item in my_list])
    
#Leetcode: Problem 129. Sum Root to Leaf Numbers
if __name__ == '__main__':
    sol = Solution()
    myBT = BinarySearchTree()

    inputs = [19, 7, 43, 3, 11, 23, 47, 2, 5, 37, 53, 29, 41, 31]
    
    for input in inputs:
        myBT.insert(input)
        
    print(f"Sum is: {sol.sumNumbers(myBT.get_root())}")