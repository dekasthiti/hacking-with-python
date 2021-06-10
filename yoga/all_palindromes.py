def get_palindromes(in_string):
    p_list = set()
    len_str = len(in_string)
    
    # in_string: "" or "a"
    if len_str <= 1:
        p_list.add(in_string)
    else:
        for i in list(range(1, len_str)):
            if in_string[i] == in_string[i - 1]:
                # Slicing excludes the end index, hence +1
                p_list.add(in_string[i-1: i+1])
                left = 1
            else:
                left = 0
                
            if i > len_str // 2:
                j_end = len_str - i
            else:
                j_end = i

            # range excludes the last index, hence +1
            for j in list(range(1, j_end + 1)):
                if i+j >= len_str:
                    break
                if in_string[i-j-left] == in_string[i+j]:
                    p_list.add(in_string[i-j-left: i+j+1])
                else:
                    break
    sorted_list = sorted(p_list, key=lambda x: len(x), reverse = True)
    print(sorted_list)
    return p_list
    
    
if __name__ == '__main__':
    
    # Inputs: "ccc", "a", "madam",
    in_str = input("Enter the string to test")
    p_list = get_palindromes(in_str)
    print([p for p in p_list])