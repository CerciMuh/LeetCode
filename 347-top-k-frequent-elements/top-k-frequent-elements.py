class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap, num in nums will be the index and then give it number 1 and add 1 to it each time and 
        #retrun top k elements
        lookup = {}
        for num in nums: 
            if num in lookup:
                lookup[num]+=1
            else:
                lookup[num] = 1    
        return [key for key, _ in sorted(lookup.items(), key=lambda item: item[1], reverse=True)[:k]]
        