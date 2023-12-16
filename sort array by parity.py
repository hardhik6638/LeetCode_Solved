def sortArrayByParity(nums):
        return sorted(nums,key=lambda x:x%2)
nums=[int(i) for i in input().split()]
r=sortArrayByParity(nums)
print(r)



