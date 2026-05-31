class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if(n==0):
            return []
        if(n==1):
            return nums    
        if(n==2):
            nums.reverse()  
            return nums
        if(n>=3):
            output0=[]
            output1=[]
            output0.append(1)
            output0.append(nums[0])
            for i in range(n-2):
                value = nums[i+1] * output0[i+1]
                output0.append(value)
            nums.reverse()
            output1.append(1)
            output1.append(nums[0])
            for i in range(n-2):
                value = nums[i+1] * output1[i+1]
                output1.append(value)  
            output1.reverse()    
            list_to_be_returned = []
            for i in range(n):
                list_to_be_returned.append(output0[i] * output1[i])

            return list_to_be_returned    
        
