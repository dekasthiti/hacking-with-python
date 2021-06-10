from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        
        if nums:
            mid_point = len(nums) // 2 - 1 if len(nums) % 2 == 0 else len(nums) // 2
            
            if nums[mid_point] == target:
                start = end = mid_point
                
                if mid_point > 0:
                    # if nums[mid_point - 1] == target:
                    #     start, _  = self.searchRange(nums[0:mid_point], target)
                    i = mid_point
                    while i > 0:
                        if nums[i - 1] == target:
                            i -= 1
                        else:
                            break
                    start = i

                    
                    # if nums[mid_point + 1] == target:
                    #     _, sub_end = self.searchRange(nums[mid_point:], target)
                    #     end = end + sub_end
                    i = mid_point
                    while i < len(nums) - 1:
                        if nums[i + 1] == target:
                            i += 1
                        else:
                            break
                    end = i
            elif nums[mid_point] < target:
                offset = mid_point + 1
                start, end = self.searchRange(nums[mid_point + 1:], target)
                start += offset
                end += offset
                
            # nums[mid_point] > target
            else:
                start, end = self.searchRange(nums[0: mid_point - 1], target)
        
        return [start, end]
    
    
if __name__ == '__main__':
    sol = Solution()
    input_arr = [5,8,8,8,8,10]
    print(sol.searchRange(input_arr, target = 1))