from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        idx = 0
        len_arr = len(arr)
        prev_2_consecutive_odd = False
        while idx < len_arr:
            num = arr[idx]
            if num % 2 == 0:
                idx += 1
                continue
            # curr number is odd
            
            # In a previous iteration, if we had x_even, y_odd, z_odd and this one is w_odd
            #i.e., this num could be the end of a search window
            if prev_2_consecutive_odd:
                print("Previous 2 consecutive odd")
                print(arr[idx-2], arr[idx-1], arr[idx])
                return True
            # Otherwise, this num is the start of the search window
            if idx + 1 < len(arr):
                # odd_y, even
                if arr[idx + 1] % 2 == 0:
                    idx += 2
                    continue
                # odd_y, odd_z, ?
                if idx + 2 < len(arr):
                    # odd_y, odd_z, even
                    if arr[idx + 2] % 2 == 0:
                        idx += 3
                        continue
                    #odd_y, odd_z, odd_w
                    print(arr[idx], arr[idx+1], arr[idx+2])
                    return True
                return False
            return False
        return False
    
if __name__ == '__main__':
    sol = Solution()
    input_list = [1,2,34,3,4,5,7,23,12], [2,6,4,1],
    for input in input_list:
        if sol.threeConsecutiveOdds(input):
            print(f"3 consecutive odds in {input}")
        else:
            print(f"No 3 consecutive odds in {input}")