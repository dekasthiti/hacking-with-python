from argparse import ArgumentParser
import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if n <= 0:
            return 0  # is this strictly true? what about anding negative numbers?
            # This solution has limitation because we can't take the log of
            # negative numbers
        nearest_power_2 = math.log2(n)
        pow = int(nearest_power_2)
        # if the nearest power of 2 is greater than the start m, it is in the range & will zero out
        # the result
        if 2 ** pow > m:
            return 0
        else:
            res = m
            for i in range(m + 1, n + 1):
                res = res & i
        return res

# Leetcode: 201. Bitwise AND of Numbers Range
if __name__ == '__main__':
    sol = Solution()
    parser = ArgumentParser()
    parser.add_argument('--start', help='Start of range', type=int)
    parser.add_argument('--end', help='End of range', type=int)
    args = parser.parse_args()
    print(f"Bitwise AND of range is: {sol.rangeBitwiseAnd(args.start, args.end)}")