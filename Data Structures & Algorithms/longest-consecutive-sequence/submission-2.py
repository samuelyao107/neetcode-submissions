class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_nums = set(nums)
        n = len(my_nums)
        global_count =0
        already_checked = set()
        for elem in my_nums:
            if elem not in already_checked :
                if (elem - 1) not in my_nums :
                    count = 1
                    while elem + 1 in my_nums:
                            already_checked.add(elem + 1)
                            count +=1
                            elem +=1  
                    if count > global_count:
                        global_count = count
        return global_count
                    


       


