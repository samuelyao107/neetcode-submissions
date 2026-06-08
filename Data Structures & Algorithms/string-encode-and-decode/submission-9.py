class Solution:

    def encode(self, strs: List[str]) -> str:
        n=len(strs)
        if n>1:
            encoded = strs[0]
            for i in range(1,n):
                if i !=n-1:
                    encoded += "€"+strs[i]
                else:
                    encoded += "€"+strs[i]+"€"    
            print(encoded)    
            return encoded
        if strs == []:
            return "€"
        if strs == [""]:
            return ""       
        return strs[0]    

    def decode(self, s: str) -> List[str]:
        if s== "€":
            return []
        n= len(s)
        j=0
        decoded=[]
        if "€" in s and n>1:
            word =[]
            while j < n :
                if s[j] != "€":
                    word.append(s[j])
                else:
                    decoded.append("".join(word))
                    word = []
                j+=1  
            return decoded      
        
        return [s]     
