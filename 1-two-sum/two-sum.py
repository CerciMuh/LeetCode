class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #force solution 
        hashmap = {}
        for  i in range(len(nums)):
            if target - nums[i] in hashmap:
                return (i,hashmap.get(target-nums[i]))
            else:
                hashmap[nums[i]] = i

        #now optimize using a hashmap
        # each time we visit a number store it in a hashmap 
        #we start with an empty and start populating the hashmap
        #one might think u are just rebuilding the list but no hashmap is direct lookup (key,value pair)
        