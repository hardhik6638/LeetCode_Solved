nums=[int(i) for i in input().split()]
k=int(input())
n=len(nums)
maxi=max(nums)
i,j,cnt,ans=0,0,0,0
while j<n:
    if nums[j]==max:
        cnt+=1
    if cnt>=k:
        while cnt>=k:
            ans+=n-j
            if nums[i]==maxi:
                cnt-=1
            i+=1
    j+=1
print(ans)

