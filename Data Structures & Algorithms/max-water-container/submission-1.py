class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max=0
        i=0
        j=n-1
        while i!=j :
            min_elem = min(heights[i], heights[j])
            value = min_elem * abs(i-j)
            if value> max:
                max = value
            if min_elem == heights[i]:
                i+=1
            else:
                j -=1   
        return max         

        