class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # do for loop to fix a number 
    # treat other 2 numbers as a 2 sum problem 
    # regardless of order (im guessing a set) 
    # will solve later im practically fried today
        nums.sort()
        result = []
        for i,num in enumerate(nums):
            if (i>0 and num == nums [i-1]):
                 continue
            l =i+1
            r= len(nums)-1
            while(l<r):
                threeSum = num + nums[l]+nums[r]
                if threeSum == 0:
                    result.append([num,nums[l],nums[r]])
                    l+=1
                    while (l<r and nums[l] == nums[l-1]):

                        l+=1

                elif threeSum > 0 : 
                    r-=1
                elif threeSum<0:
                    l+=1       
                    
        return result