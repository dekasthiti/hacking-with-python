from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # If nums is [] or [1], nums[0], nums[1] will give index out of range, but nums[1:] is an empty list and
        # doesn't raise exception!
        # sum_right = sum(nums[1:])
        sum_right = sum(nums)
        sum_left = 0
        for idx, num in enumerate(nums):
            sum_right -= num
            # print(f"Left of {num}: {sum_left} ")
            # print(f"Right of {num}: {sum_right} ")
            if sum_left == sum_right:
                return idx
            sum_left += nums[idx]
        return -1
    
# Leetcode: Problem 724. Find Pivot Index
if __name__ == '__main__':
    sol = Solution()
    nums_list = [], [1],[1,2,3], [1,7,3,6,5,6], [-1,-1,-1,0,1,1]
    for nums in nums_list:
        print(sol.pivotIndex(nums))