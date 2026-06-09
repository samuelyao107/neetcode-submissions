class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict0={}
        n=len(numbers)
        for i in range(n):
            if target-numbers[i] in dict0:
                return [dict0[target-numbers[i]]+1, i+1]
            else:
                dict0[numbers[i]]=i

        return []      
