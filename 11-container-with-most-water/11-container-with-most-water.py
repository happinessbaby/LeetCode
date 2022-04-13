class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)-1
        l,r=0,0
        area = []
        while True:
            if l==len(height)-1-r:
                break
            if height[l]<=height[len(height)-1-r]:
                area.append(length*height[l])
                l+=1
            else:
                area.append(length*height[len(height)-1-r])
                r+=1
            length-=1
        return max(area)