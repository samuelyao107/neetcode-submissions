class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        if len(nums) ==1:
            return nums    
        prefix = [1]
        suffix=[1]
        for i in range(len(nums)-1):
            prefix.append(prefix[i]*nums[i])    
        print(prefix)
        nums.reverse()

        for i in range(len(nums)-1):
            suffix.append(suffix[i]*nums[i])
        suffix.reverse()    
        output = []
        for i in range(len(prefix)):
            output.append(prefix[i]*suffix[i])
        return output    
        



        