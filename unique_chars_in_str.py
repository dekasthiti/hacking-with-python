def unique_chars(inp_str: str)->bool:
    if inp_str:
        unique_chars_set = set()
        for letter in inp_str:
            if letter in unique_chars_set:
                return False
            else:
                unique_chars_set.add(letter)

    return True


inp_str = "hello"
is_unique_chars = unique_chars(inp_str)
print(f"Does \"{inp_str}\" have unique chars?\n{is_unique_chars}")
