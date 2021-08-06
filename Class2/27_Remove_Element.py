from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.nums=nums
        self.val=val
        
        c=0
        n=len(nums)
        for i in range(0,n,1):
            if nums[i]==val:
                nums[i]= '_'
            else:    
                c+=1
        
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                if nums[i]=='_':
                    t=nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
                
        print(nums[:c])
        return(c)        

p=Solution()       
print(p.removeElement([4,5],4))
