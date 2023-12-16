class Solution:
    def findMaxK(self, nums: list[int]):
        # first approach
        '''l,r=0,len(nums)-1
        nums.sort()
        while l<r:
            if -nums[l] == nums[r]:
                return nums[r]
            elif -nums[l]>nums[r]:
                l+=1
            else:
                r-=1
        return -1'''
        #second approach
        nums=sorted(nums,reverse=True)
        s=set(nums)
        for i in range(len(nums)):
            if -nums[i] in s:
                return nums[i]
        return -1

