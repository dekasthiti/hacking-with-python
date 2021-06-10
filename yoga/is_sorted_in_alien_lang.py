from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # # Encode the alphabet
        # letter_encoding = {letter: i + 1 for i, letter in enumerate(order)}
        
        # Encode the words
        from collections import defaultdict
        word_encoding = defaultdict(list)
        for word in words:
            # word_encoding[word] = [letter_encoding[letter] for letter in word]
            word_encoding[word] = [order.index(letter) for letter in word]
            
        print(word_encoding)
        
        words_list_len = len(words)
        
        sorted = True
        
        # Since we are looking ahead, need to iterate over words_list_len-1, and can't achieve this by enumerating
        # over the dict
        for idx, (word, enc) in zip(range(words_list_len - 1), word_encoding.items()):
        # for idx, (word, enc) in enumerate(word_encoding.items()):
            curr_word_enc = enc
            next_word_enc = word_encoding[words[idx + 1]]

            print(f"{words[idx]} : {curr_word_enc}")
            print(f"{words[idx+1]} : {next_word_enc}")
            
            if curr_word_enc > next_word_enc:
                sorted = False
                break
        
        return sorted
    
    
        # # Alternative solution, takes abt the same time, same memory
        # for i in range(len(words) - 1):
        #     word1 = words[i]
        #     word2 = words[i + 1]
        #
        #     if len(word1) <= len(word2) and word1 in word2:
        #         continue
        #     if len(word1) > len(word2) and word2 in word1:
        #         return False
        #
        #     for ch1, ch2 in zip(word1, word2):
        #         if order.index(ch1) > order.index(ch2):
        #             return False
        #         elif order.index(ch1) == order.index(ch2):
        #             continue
        #         else:
        #             break
        #
        # return True
    
    
if __name__ == '__main__':
    sol = Solution()
    words = ['abc', 'hello', 'world']
    order = 'hlabcdefgijkmnopqrstuvwxyz'
    print(sol.isAlienSorted(words, order))