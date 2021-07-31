from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int)-> List[int] :
        self.nums=nums
        self.target=target
        n=len(nums)
        for i in range(0,n):
            x= target- nums[i]
            for j in range(i+1,n):
                if nums[j]==x:    
                  p=i  
                  q=j  
                j+=1
            i+=1    
        return [p,q]
