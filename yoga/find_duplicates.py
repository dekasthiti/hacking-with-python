from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        limit = len(nums)
        for i in range(limit):
            if (i + 1) > sorted_nums[i]:
                return (sorted_nums[i])
    
# Leetcode: Problem 287. Find the Duplicate Number
# This solution did better than 98% of submissions on memory
if __name__ == '__main__':
    sol = Solution()
    
    # See how you can have a list (or is this a tuple?) without enclosing braces?
    
    nums_list = [3,1,3,4,2], [1,3,4,2,2], [1,1], [1,1,2], list(range(1,2000)) + [400]
    
    # This is a tuple
    print(type(nums_list))
    for nums in nums_list:
        print(f"Duplicate is: {sol.findDuplicate(nums)}")