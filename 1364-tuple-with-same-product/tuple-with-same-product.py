class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        tuples = {}
        for i,num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                product = nums[i]*nums[j]
                if product in tuples:
                    tuples[product] +=1
                else:
                    tuples[product] = 1

        result = 0 
        print (tuples)
        for i in tuples.values():  
            if i > 1:
                result += (i*(i-1)//2) * 8           

        return result