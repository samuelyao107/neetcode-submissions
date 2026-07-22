class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        if len(s) < 2:
            return len(s)    

        output = set()
        i=0
        j=1
        output.add(s[i])
        while i<len(s) and j<len(s):
            if s[j] not in output:
                output.add(s[j])
                j+=1
            else:
                if len(output)>max:
                    max = len(output)   
                output.remove(s[i])
                i+=1
                if i == j:
                    output.add(s[j])
                    j+=1 
        if len(output)>max:
            max = len(output)
        return max             

        '''    max=0
        if len(s) < 2:
            return len(s)    

        output = set()
        i=0
        j=1
        output.add(s[i])
        while i<len(s) and j<len(s):
            if s[j] not in output:
                output.add(s[j])
                j+=1
            else:
                if len(output)>max:
                    max = len(output)   
                output=set()
                i+=1




































$0
                j=i+1 
                output.add(s[i])
        if len(output)>max:
            max = len(output)

        return max '''
         

