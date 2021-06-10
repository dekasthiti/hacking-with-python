from collections import namedtuple
class Solution:
    
    @staticmethod
    def find_adj_duplicates(S: str):
        
        # Named tuple can be handy, but didn't work in this case because the input string keeps changing,
        # and so will the start, end indices
        Dup_indices = namedtuple('dup_letter', 'letter, count')
        dup_indices_list = []
        start = end = 0
        while start < len(S) - 1:
            curr = start
            next = curr + 1
            while next < len(S) and S[curr] == S[next]:
                next += 1
            
            if next - curr > 1:
                dup_indices_list.append(Dup_indices(letter = S[start], count = next - curr))
            start = next
            
        return dup_indices_list
            
    def removeDuplicates(self, S: str) -> str:
        
        # new_str = S
        # This won't work because the input string keeps changing, so the indices won't be relevant
        # dup_indices_list = self.find_adj_duplicates(S)
        # for dup_letter, count in dup_indices_list:
        #
        #     new_str = S.replace(dup_letter, '', count)
        #     S = new_str
        # return new_str
        #
        
        # Using str.replace() doesn't work when you want to work between specific indices
        
        # idx = 0
        # while idx < len(S) - 1:
        #     # Look ahead 1 character
        #     curr_letter = S[idx]
        #     if S[idx] == S[idx + 1]:
        #         # # Want to replace 'aa', not any 'a' as, hence, S[idx]+S[idx+1]
        #         # new_str = S.replace(S[idx] + S[idx+1], '', 1)
        #         # # However, this doesn't work when we have odd number of repeated characters like 'aaa' - it'll
        #         # # leave behind the last 'a'
        #         # When you want to delete characters at an index, of a certain count, slice and concat
        #         # may be the only way that works
        #         S = S.replace(S[idx] + S[idx+1], '', 1)
        #         # Check if there is one remaining letter
        #         if curr_letter == S[idx]:
        #             S = S[:idx] + S[idx+1:]
        #         # This replacing would have created another substring with duplicate characters,
        #         # so, look back 1 character
        #         if idx > 0 and S[idx] == S[idx-1]:
        #             S = S.replace(S[idx - 1] + S[idx], '', 1)
        #             idx -= 1
        #     else:
        #         idx += 1
        #
        
        idx = 0
        while idx < len(S) - 1:
            start_idx = idx
            end_idx = start_idx + 1
            while S[start_idx] == S[end_idx]:
                end_idx += 1
                # Heuristics: If the search took you till the end of the string, you will delete
                # everything and return an empty string. Ex: 'aaaaa'
                # So, break if adj characters are not the same, or, you reached the end of the string
                if end_idx == len(S):
                    return S[:start_idx]
            
            if end_idx - start_idx > 1:
                # remove everything between start and end index
                S = S[:start_idx] + S[end_idx:]
                
                # This concat might have introduced more adjacent duplicates, look 1 step back
                if idx > 0 and S[idx] == S[idx - 1]:
                    # reset the index
                    idx -=1
            else:
                idx += 1
                
        return S
if __name__ == '__main__':
    # Leetcode: 1047 - Remove all adjacent duplicates in string
    sol = Solution()
    S = "aaaaaaaaa" #"aababaab" #'aabaabccaa' # 'aaaaa' #
    trimmed_S = sol.removeDuplicates(S)
    print(f"Original string: {S}, Trimmed string: {trimmed_S}")