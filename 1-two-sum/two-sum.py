class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            curr = nums[i]
            if target - curr not in hashmap:
                hashmap[curr] = i 
            else:
                return [i,hashmap[target-curr]]
            
            