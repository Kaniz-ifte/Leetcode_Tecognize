from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums=nums
        self.target=target
        
        c=0
        n=len(nums)
        if (target in nums):
            for i in range(0,n,1):
                if nums[i]==target:
                    c=i
        else:
            for i in range(0,n,1):
                if nums[i]<target:
                    c=i+1
                else:    
                    break
                
        return c           

p=Solution()       
print(p.searchInsert([1,3,5,6],2))
