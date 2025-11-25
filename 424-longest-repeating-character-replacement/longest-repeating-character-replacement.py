class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window, start from left count first character then keep moving then k different letters appear, that would be ourrr max length. when k different are detected. slide one position to right do same process.
        left = 0 
        right = 1
        counts = {}
        maxFreq = 0 
        maxLen = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right],0) + 1
            maxFreq = max(maxFreq,counts[s[right]])
            while right - left +1 - maxFreq >k:
                counts[s[left]] -=1
                left+=1
            maxLen = max(maxLen, right - left + 1)

        return maxLen