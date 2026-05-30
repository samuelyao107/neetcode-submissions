class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict0={}
        for elem in nums:
            if elem in dict0:
                dict0[elem] +=1
            else:
                dict0[elem] = 1
        n=len(nums)
        my_list = [[] for _ in range(n)]  
        for elem in dict0:
            my_list[dict0[elem]-1].append(elem)   
        list_to_be_returned = []
        i=k
        for elem in reversed(my_list):    
            if elem != [] :
                for num in elem:
                 list_to_be_returned.append(num)
                 i -=1
            if i==0 :
                return  list_to_be_returned
        return list_to_be_returned          



