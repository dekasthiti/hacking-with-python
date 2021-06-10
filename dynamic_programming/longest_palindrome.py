
class Solution:
    def __init__(self):
        self.palindromes = set()
        self.not_palindrome = set()
        pass
        
    def find_palindromes(self, str):
        # Already detected this substring as a palindrome
        if str in self.palindromes:
            return True
    
        # Already seen this substring and marked it as not a palindrome
        elif str in self.not_palindrome:
            return False
        
        if len(str) == 1:
            self.palindromes.add(str)
            return True
        
        if len(str) == 2:
            if str[0] == str[1]:
                self.palindromes.add(str)
                return True
            else:
                return False
        
        # Not seen this before, do palindrome check for first & last letters & recurse
        try:
            center_part = str[1:-1]
            left_part = str[0:-1]
            right_part = str[1:]
            if str and str[0] == str[-1] and self.find_palindromes(center_part):
                self.palindromes.add(str)
                return True
            else:
                self.not_palindrome.add(str)

                left = self.find_palindromes(left_part)
                right = self.find_palindromes(right_part)
                if left or right:
                    if left:
                        self.palindromes.add(left_part)
                    if right:
                        self.palindromes.add(right_part)
                return False
        except IndexError as err:
            print(f"Current string is {str}")
            
            
    def find_longest_palindrome(self, str):
        self.find_palindromes(str)
        if self.palindromes:
            sorted_list = sorted(self.palindromes, key = lambda x: len(x), reverse = True)
            print(sorted_list)
            return sorted_list[0]
        else:
            return 0
    
    
if __name__ == '__main__':
    sol = Solution()
    print(f'Longest palindrome is : {sol.find_longest_palindrome("aacabdkacaa")}')