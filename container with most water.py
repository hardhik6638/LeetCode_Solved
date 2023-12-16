def maxArea(height):
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            currentarea=min(height[left],height[right])*(right-left)
            maxArea=max(maxArea,currentarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
height=[int(i) for i in input().split()]
r=maxArea(height)
print(r)




