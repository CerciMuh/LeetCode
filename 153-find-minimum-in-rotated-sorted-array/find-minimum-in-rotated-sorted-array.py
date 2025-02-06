class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums)-1
        while (left<=right):

            middle = (left+right)//2

            if nums[middle]>nums[right]:
                #312
                left = middle +1

            elif nums[middle]<nums[right]:

                right = middle 
            else:
                return nums[middle]
        
        return nums[middle]