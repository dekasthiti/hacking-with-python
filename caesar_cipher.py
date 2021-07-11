"""
Caesar Cipher (caesar.py)

A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. For example, assume the input plain text is the following:

abcd xyz
If the shift value, n, is 4, then the encrypted text would be the following:

efgh bcd
You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.
"""


def caesar_cipher(plain_text='', shift_value=0):
    new_plain_text = ''
    for letter in plain_text:
        if not letter.isalpha():
            new_plain_text += letter
        else:
            # What happens when we cross 'z' : either the shift_value is big or because we have the
            # last letters of the alphabet?
            new_plain_text += chr(ord(letter) + shift_value % 26)
    return new_plain_text


def caesar_cipher_with_stdlib(plain_text='', shift_value=0):
    import string
    # 1. First, create a translation table with the shift
    # Create the translation map
    letters = string.ascii_lowercase
    shifted_letters = letters[shift_value:] + letters[:shift_value]
    translation_table = str.maketrans(letters, shifted_letters)
    return plain_text.translate(translation_table)


def caesar_cipher_with_custom_transtab(plain_text='', shift_value=0):
    import string
    
    def shift_n(letter, n):
        n = n % 26
        translation_table = string.ascii_lowercase[n:] + string.ascii_lowercase[:n]
        try:
            # Find position of the letter in the original alphabet
            index = string.ascii_lowercase.index(letter)
            
            # Find the corresponding letter in the destination alphabet
            translated_character = translation_table[index]
            return translated_character
        except IndexError:
            return letter
       
    enc_list = [shift_n(letter, shift_value) for letter in plain_text]
    return ''.join(enc_list)


def main():
    plain_text = 'hello'
    
    assert caesar_cipher(plain_text, 4) == caesar_cipher_with_custom_transtab(plain_text, 4) == caesar_cipher_with_stdlib(plain_text, 4) == 'lipps'
    #
    print(f'Cipher for {plain_text} is {caesar_cipher(plain_text, 4)}')
    print(f'Cipher for {plain_text} is {caesar_cipher_with_stdlib(plain_text, 4)}')
    print(f'Cipher for {plain_text} is {caesar_cipher_with_custom_transtab(plain_text, 4)}')
    
    
if __name__ == '__main__':
    main()

