class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0
        explored = {}

        for right in range(len(s)):
            char = s[right]
            if char in explored and explored[char] >= left:
                left = explored[char] + 1  
            explored[char] = right  
            best = max(best, right - left + 1)  

        return best