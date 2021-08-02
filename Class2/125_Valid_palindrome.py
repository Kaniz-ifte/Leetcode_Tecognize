import re
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s=s
        
        #s=s.lower()
        #s=re.sub(r'[^\w\d\s]+','',s)
        s=''.join([i.lower() for i in s if i.isalnum()])
        #s=s.replace(' ','')
        print(s)
        
        start=0
        end=len(s)-1
        
        
        while start<end:
          if s[start]!=s[end]:
             return False
          
          start+=1
          end-=1   
        return True
      
p=Solution()       
print(p.isPalindrome("0p"))      
