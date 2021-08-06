from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        self.nums=nums
        
        c=0
        n=len(nums)
        for i in range(0,n-1,1):
            for j in range(i+1,n-1,1):
                if nums[i]==nums[j]:
                    nums[j]= nums[n-1]
                else:
                    break
              
            
        nums.sort()

        for i in range(0,n,1):
            c+=1
            if nums[i]==nums[n-1]:
                break

        print(nums[:c]) 
        return c
