# ONE PASS
def twoSum( nums, target):
        prevmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevmap:
                lst_= [prevmap[diff],i]
            prevmap[n]=i
        print(lst_)
nums=[int(i) for i in input().split()]
target=int(input())
twoSum(nums,target)

