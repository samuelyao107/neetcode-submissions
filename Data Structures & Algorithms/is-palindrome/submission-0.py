import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        n=len(s)  
        for i in range(n):
            if s[i] != s[n-1-i]:
                return False
        return True        
        