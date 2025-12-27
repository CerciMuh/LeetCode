class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # this will be of O(n) because we will have to loop within all of the list and fix each number entry then do a 2 sum problem with the fixed number to be considered within the summation. before doing all of this we will need to sort the nums to be able to do the 2Sum problem properly 
        nums.sort()
        result = set()
        for i in  range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                x = nums[l]+nums[r]+nums[i]
                if x== 0:
                    result.add((nums[l],nums[r],nums[i]))
                    l+=1
                    r-=1
                elif x > 0:
                    r-=1
                elif x < 0 :
                    l+=1
        return[list(t) for t in result]
