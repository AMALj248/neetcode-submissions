class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # old code
        # max_len = 0
        # i, j = 0, 0
        # char_map = {}
        # n = len(s)
        # while(i<=j<n):
        #     sub_str = s[i:j+1]
        #     if s[j] not in char_map:
        #         curr_len = len(sub_str)
        #         max_len = max(curr_len, max_len)
        #         char_map[s[j]]=j
        #         j+=1
        #     else:
        #         i = max(i, char_map[s[j]] + 1)
        #         char_map[s[j]] = j
        #         curr_len = j - i + 1
        #         max_len = max(max_len, curr_len)
        #         j+=1
        # return max_len
        max_len = 0
        i = 0
        char_map = {}

        for j, char in enumerate(s):
            if char in char_map:
                i = max(i, char_map[char] + 1)

            char_map[char] = j
            max_len = max(max_len, j - i + 1)

        return max_len





            
