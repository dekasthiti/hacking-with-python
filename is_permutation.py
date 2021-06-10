# This solution is case and space sensitive
def is_permutation(inp_str1: str, inp_str2: str)-> bool:
    if inp_str1 and inp_str2:
        if len(inp_str1) == len(inp_str2):
            char_count_dict = {}

            # First pass: Iterate over the chars of str1, count up the letters
            for letter in inp_str1:
                if letter in char_count_dict.keys():
                    count = char_count_dict[letter]
                    char_count_dict[letter] = count+1
                else:
                    char_count_dict[letter] = 1

            # Second pass: Iterate over the chars of str2, count down the letters
            # If any letter count drops below zero, exit early
            for letter in inp_str2:
                if letter in char_count_dict.keys():
                    count = char_count_dict[letter]
                    # This char has occurred one too many times in str2
                    if count == 0:
                        return False
                    char_count_dict[letter] = count-1
                else:
                    # char in str2 not in str1
                    return False

            # Check if the same letters appear in both the strings
            # Pass 1 counted up, Pass2 counted down, we should have 0 count for all letters
            # in the dict
            for letter, count in char_count_dict.items():
                if count != 0:
                    return False
            return True
        # str1, str2 lengths are different
        else:
            return False
    # str1 or str2 or both are None
    else:
        return False


str1 = "2hello1  "
str2 = "1olleh2"
is_permutation = is_permutation(str1, str2)
print(f"Is {str1} a permutation of {str2}: {is_permutation}")