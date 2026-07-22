class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        dict0 = {}
        for i in range(len(nums)):
            if target - nums[i] in dict0 :
                return [dict0[target - nums[i]], i]
            dict0[nums[i]] = i     

        