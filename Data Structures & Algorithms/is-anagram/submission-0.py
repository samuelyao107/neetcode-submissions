class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n = len(s)
        dict0 = {}
        dict1= {}
        for i in range(n):
            if s[i] in dict0 :
                dict0[s[i]] += 1
            else:
                dict0[s[i]] = 1

            if t[i] in dict1 :
                dict1[t[i]]+=1
            else:
                dict1[t[i]] = 1    

        for elem in dict0 :
            if elem not in dict1 or dict0[elem] != dict1[elem]:
                return False

        return True                  


