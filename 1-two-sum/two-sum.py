class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} 
        for i in range(len(nums)):
            value = nums[i]
            if value in mp:
                return [mp[value], i]
            need = target - value
            mp[need] = i
        return []
