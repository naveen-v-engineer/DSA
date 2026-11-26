nums = [0,1,0,3,12]

newList=[]
i=0
while i<len(nums):
    if nums[i]==0:
        newList.append(nums[i])
        nums.remove(nums[i])
    else:    
        i+=1

nums.extend(newList)

print(nums)


