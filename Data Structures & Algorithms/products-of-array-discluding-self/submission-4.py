class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix = [1] *n
        suffix = [1]*n

        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]

        my_list=[]
        for i in range(n):
            my_list.append(suffix[i]*prefix[i])

        return my_list    
