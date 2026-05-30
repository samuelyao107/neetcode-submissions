from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict0= defaultdict(list)
        for elem in strs:
            compt = [0]*26
            for letter in elem: 
                n = ord(letter) - 97
                compt[n]+=1  
            key = tuple(compt)
            dict0[key].append(elem)
            
        to_be_returned=[]
        for list_elem in dict0.values():
            to_be_returned.append(list_elem)
        return to_be_returned    
