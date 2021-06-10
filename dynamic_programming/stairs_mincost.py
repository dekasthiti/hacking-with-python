from typing import List

"""
746. Min Cost Climbing Stairs

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_memo = [0 for _ in cost]
        cost_memo[0] = cost[0]
        if len(cost) > 1:
            cost_memo[1] = min(cost[0], cost[1])
        if len(cost) > 2:
            cost_memo[2] = min(cost[1], cost[2] + cost_memo[0])
        staircase_len = len(cost)
        for i in range(3, staircase_len):
            # You reach staircase 10 either by jumping 1 step or 2 steps:
            # 1. Paying for staircase 10 while at staircase 9 and jumping 1 step, or,
            # 2. Paying for staircase 9 while at staircase 8 and jumping 2 steps

            cost_memo[i] = min(cost[i] + cost_memo[i-1],
                               cost[i - 1] + cost_memo[i-2])
            
            # cost_memo[i] = min(cost[i] + cost_memo[i-2], cost_memo[i-1])
                
        return cost_memo[-1]
        
if __name__ == '__main__':
    sol = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    #cost = [10, 15, 20]
    print(f'Min cost to get to the top of the staircase: {sol.minCostClimbingStairs(cost)}')
    
