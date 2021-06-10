class Solution:
    def __init__(self):
        super(Solution).__init__()
    
    def find_max_price(self, lengths, prices):
        price_memo = [[0 for _ in lengths] for _ in prices]
        total_len = len(lengths)
        for i in lengths:
            # There is no point inspecting the price of a rod piece whose length is greater than the rod length under
            # inspection
            for j in lengths:
                if j > i:
                    break
                if i == j:
                    # indexing with i-1, j-1 because lengths are starting with 1 while arrays are 0-indexed
                    price_memo[i-1][j-1] = prices[j-1]
                else:
                    price_memo[i-1][j-1] = max(price_memo[i-j-1]) + max(price_memo[j-1])
        return max(price_memo[total_len - 1])
    
    
if __name__ == '__main__':
    sol = Solution()
    lengths = [1, 2, 3, 4, 5, 6, 7, 8]
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(f"Max price: {sol.find_max_price(lengths, prices)}")