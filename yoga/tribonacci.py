class Solution:
    def tribonacci(self, n: int) -> int:
        trib = []
        trib.append(0)
        trib.append(1)
        trib.append(1)
        for i in range(3, n):
            trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])
        
        if n > 2: #why are you adding again?
            return trib[n - 1] + trib[n - 2] + trib[n - 3]
        else:
            return trib[n]

if __name__ == '__main__':
    sol = Solution()
    number = input("Enter n whose tribonacci you want to compute")
    print(f"Tribonacci of {number} is {sol.tribonacci(int(number))}")
    