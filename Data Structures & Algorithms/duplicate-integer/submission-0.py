class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict0={}
        for elem in nums:
            if elem in dict0:
                dict0[elem] +=1
            else:
                dict0[elem] = 1

        for elem in dict0:
            if dict0[elem] > 1 :
                return True
        return False                    