import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #I think I have the nicest solution to this
        #we will have a hashmap
        #we will also have a variable called value because I have no idea what it stands for
        #
        heap = []

        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        