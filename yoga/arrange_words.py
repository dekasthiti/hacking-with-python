from collections import defaultdict, namedtuple
class Solution:
    def arrangeWords(self, text: str) -> str:
        rearranged_words = ''
        
        # dict will not work for a sentence like "To be or not to be"
        # because it will merge "be"
        #letter_count = defaultdict(int)
        LetterCount = namedtuple('letter_count', 'word, count')
        letter_count_list = []
        text_list = text.split(' ')
        for word in text_list:
            # letter_count[word] = len(word)
            letter_count_list.append(LetterCount(word = word.lower(), count = len(word)))
        
        #print(letter_count)
        # print(letter_count_list)
        
        # Sorting a dict/tuple by values
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        # sorted_letter_count = sorted(letter_count.items(), key = lambda item: item[1])
        sorted_letter_count = sorted(letter_count_list, key = lambda item: item[1])

        # print(sorted_letter_count)
        
        for word, count in sorted_letter_count:
            rearranged_words += word + ' '
            
        # The first letter of the sentence is upper case
        rearranged_sentence = rearranged_words[0][0].upper() + rearranged_words[1:]
        
        # Remove the last space in the sentence
        return rearranged_sentence.rstrip( )
        
        
# Leetcode: Problem 1451: Rearrange Words in a Sentence
if __name__ == '__main__':
    sol = Solution()
    text = ["To be or not to be", "Keep calm and code on", "Leetcode is very cool"]
    for sentence in text:
        rearranged_sentence = sol.arrangeWords(sentence)
        print(rearranged_sentence)