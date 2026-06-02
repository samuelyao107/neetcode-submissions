class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        nums.sort()
        my_set = set()
        i=0
        j= n-1
        while i < n-1 :
                value = -nums[i]-nums[j]
                #another_set= set(nums[i+1:j])
                if value in nums[i+1:j]:
                        my_set.add((nums[i],value,nums[j]))
                j-=1        
                if(i==j):
                    i+=1
                    j=n-1

        output=[]            
        for elem in my_set:       
            output.append(list(elem))
        return output    