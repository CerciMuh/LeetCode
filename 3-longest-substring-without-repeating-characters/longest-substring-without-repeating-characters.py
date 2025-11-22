class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0 
        seen = []
        maxLen = 0
        currLen = 0 
        while (right < len(s)):
            if s[right] not in seen:
                seen.append(s[right])
                maxLen = max(maxLen,right-left+1)
                right+=1 
            else: 
                seen.remove(s[left])
                left+=1
        return maxLen