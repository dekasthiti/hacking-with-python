from yoga.trees.insert_and_delete import BinarySearchTree
from yoga.trees.insert_and_delete import BinaryTreeNode

import random


def is_equal(T1: BinaryTreeNode, T2:BinaryTreeNode) ->bool:
    if T1 and T2 and T1.val == T2.val:
        if T1.left and T2.left:
            is_equal(T1.left, T2.left)
        else:
            return False
        if T1.right and T2.right:
            is_equal(T1.right, T2.right)
        else:
            return False
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    T1 = BinarySearchTree()
    T2 = BinarySearchTree()

    random.seed(0)
    
    inputs_T1 = [random.randint(1, 50) for _ in range(10)]
    inputs_T2 = [random.randint(1, 50) for _ in range(10)]
    for i in inputs_T1:
        T1.insert(i)
    for i in inputs_T2:
        T2.insert(i)
        
    status = "equal" if is_equal(T1.get_root(), T2.get_root()) else "not equal"
    
    print(f"T1 and T2 are: {status}")