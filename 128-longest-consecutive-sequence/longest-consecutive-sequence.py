class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxSeq = 0
    
        for num in hashset:
            if num - 1 not in hashset:     
                curr = num
                currSeq = 1
    
                while curr + 1 in hashset:
                    curr += 1
                    currSeq += 1
    
                maxSeq = max(maxSeq, currSeq)
    
        return maxSeq