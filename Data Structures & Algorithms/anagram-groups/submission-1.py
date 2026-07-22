class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict0= {}
        for elem in strs:
            list0 = [0]*26
            for letter in elem :
                index = ord(letter) - ord('a')
                list0[index]+=1
            if tuple(list0) in dict0:
                dict0[tuple(list0)].append(elem)
            else:
                dict0[tuple(list0)] = [elem]
        output = []
        for elem in dict0:
            output.append(dict0[elem])   
        return output    

        