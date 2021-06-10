import sys
class Solution():
    def longest_unique_substring(self, input_str):
        max_substring = ''
        
        unique_substring = ''
        
        for letter in input_str:
            if letter not in unique_substring:
                unique_substring += letter
            else:
                if len(unique_substring) > len(max_substring):
                    max_substring = unique_substring
                # Update substring to strip off the duplicate letter from the beginning
                unique_substring = unique_substring[unique_substring.index(letter)+1:] + letter
        # If the last iteration had a unique character, unique_substring will have an extra letter
        # and if it happens that this extra letter made it the longest substring, we have to
        # update the max_substring
        if len(unique_substring) > len(max_substring):
            max_substring = unique_substring
            
        return len(max_substring)
    
    
def main(argv):
    input_string = argv[1] or input("Enter input string")
    print(f"Input string is {input_string}")
    sol = Solution()
    # Repeating to instrument the call stack
    for i in range(100000):
        length = sol.longest_unique_substring(input_string)
    print(f"Length of longest substring: {length}")


if __name__ == '__main__':
    main(sys.argv)
