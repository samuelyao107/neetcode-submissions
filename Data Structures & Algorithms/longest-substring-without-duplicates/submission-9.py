class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        my_set=set()
        count = 1
        max=0
        i=0
        if len(s) <2:
            return len(s);  
        i=0
        j=1
        my_set.add(s[i])
        while i< n and j < n :
            if s[j] not in my_set:
                my_set.add(s[j])
                count +=1
                j+=1
            else:
                #if count > max:
                    #max = count 
                my_set.remove(s[i])
                count -=1
                i+=1
               # my_set.add(s[i])
            if count > max:
                max = count    
         
        return max            
                


                

        