class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_nums = set(nums)
        n = len(my_nums)
        global_count =0
        for elem in my_nums:
            if (elem - 1) not in my_nums :
                count = 1
                loop_count = 0
                while loop_count<n :
                    if elem +1 in my_nums :
                        count +=1
                        elem +=1
                    loop_count +=1    
                if count > global_count:
                    global_count = count
        return global_count
                    


       


