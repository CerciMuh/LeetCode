class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        longestStreak = 1

        numSet = set(nums)

        for num in numSet:

            currentNum = num
            streak = 1 
            if num-1 not  in numSet:
                while currentNum + 1 in numSet:
                    streak+=1
                    currentNum+=1
            longestStreak = max(streak,longestStreak)

        return longestStreak