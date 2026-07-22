class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict0 = {}
        dict1 = {}
        for elem in nums:
            dict0[elem] = 0
        for elem in nums:
            if elem - 1 not in dict0:
                dict1[elem] = 1

        for elem in dict1:
            num = elem
            while num + 1 in dict0:
                dict1[elem] +=1 
                num +=1

        max = 0
        for elem in dict1:
            if dict1[elem] > max:
                max = dict1[elem]
        return max                


