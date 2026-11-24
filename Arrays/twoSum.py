nums = [2,7,11,15,3,6]
target = 9

count=0
length=len(nums)
while count<length:
    i=count+1
    while i<length:
        val=nums[count]+nums[i]
        if val==target:
            print(count,i)
        i+=1
    count+=1



        

