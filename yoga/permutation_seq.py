from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        original_number = ''.join([str(i) for i in range(1, n+1, 1)])
        target_number = ''
        i = 1
        
        # Since we are 0 indexed
        k = k - 1
        while i <= n:
            # factorial(n-i) gives us the size of the arrangements possible keeping the first digit fixed
            # For eg, when n = 3, i = 1, n-i = 2
            # 123
            # 132 are the 2 numbers possible keeping 1 in the 1st place
            # This repeats for all arrangements. In my algo, this is the set size, and we have set indices
            den = factorial(n - i)
            curr_set_index = k // den
            
            print(f"Original number: {original_number}")
            print(f"Target number: {target_number}")
            print(f"Current index: {curr_set_index}")
            
            next_set_index = k % den
            
            print(f"Digit at current index: {original_number[curr_set_index]}")
            target_number += original_number[curr_set_index]
            
            # drop the digit at the current_set_index from the original string and add it to the target string
            original_number = ''.join(original_number.split(original_number[curr_set_index]))
            
            i += 1
            k = next_set_index
        return target_number
    

if __name__ == '__main__':
    sol = Solution()
    n = input("Get number of integers")
    k = input("Get the index of the permutation you want")
    number = sol.getPermutation(int(n), int(k))
    print(f"Number is: {number}")
    
    # LEARNING: Came up with this algo purely by observing trends with 123, 1234 numbers and checking every
    # possibility in there. Once I proved that the algo works, I could also explain why it works.
