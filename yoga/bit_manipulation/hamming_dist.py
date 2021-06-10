from argparse import ArgumentParser

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp = x ^ y # Find bits that are different
        return bin(tmp).count('1')
    
#461. Hamming Distance
if __name__ == '__main__':
    sol = Solution()
    parser = ArgumentParser()
    parser.add_argument('--first_num', help = 'First number', type = int, default=20000)
    parser.add_argument('--second_num', help = 'Second number', type = int, default=247483647)
    args = parser.parse_args()
    print(f"Hamming distance: {sol.hammingDistance(args.first_num, args.second_num)}")