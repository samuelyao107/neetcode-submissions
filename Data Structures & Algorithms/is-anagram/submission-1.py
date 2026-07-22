class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict0 = {}
        dict1 = {}
        if len(s) != len(t):
            return False

        for elem in s :
            if elem not in dict0:
                dict0[elem] = 1
            else:
                dict0[elem] +=1      
        for elem in t :
            if elem not in dict1:
                dict1[elem] = 1
            else:
                dict1[elem] +=1  

        for elem in dict0:
            if elem not in dict1:
                return False 
            if dict0[elem] != dict1[elem]:
                return False    
        for elem in dict1:
            if elem not in dict0:
                return False 
            if dict0[elem] != dict1[elem]:
                return False  
        return True                                   

     