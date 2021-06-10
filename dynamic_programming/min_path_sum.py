from typing import List
import random

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 2D list initialize
        cost = [[0 for _ in range(n)] for _ in range(m)]
        # Initialize first row
        cost[0] = grid[0]

        # Initialize first col
        for i in range(m):
            for j in range(n):
                cost[i][0] = grid[i][0]
        
        # Update row, col to cumulative cost
        for i in range(1, m):
            cost[i][0] += cost[i - 1][0]
        for j in range(1, n):
            cost[0][j] += cost[0][j - 1]
        
        # Compute minimum cost
        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i - 1][j] + grid[i][j], cost[i][j - 1] + grid[i][j])
        
        # Return the bottom right element
        return cost[-1][-1]
    
    
if __name__ == '__main__':
    grid = input("Enter size of the path matrix") # 2D grid
    rows, cols = tuple(grid.lstrip(' ').split(' '))
    grid_2d = [[random.randint(1, 10) for _ in range(int(cols))] for _ in range(int(rows))]
    print(grid_2d)
    sol = Solution()
    print(f"Minimum cost: {sol.minPathSum(grid_2d)}")