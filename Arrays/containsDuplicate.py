nums = [1,2,3,1]

count=0

result=False

while count<len(nums):
    i=count+1
    while i<len(nums):
        if(nums[count]==nums[i]):
            result=True
            break
        i+=1
    count+=1

print(result)

            
