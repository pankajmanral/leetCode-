'''

here,
    the indexing is starting from 1 to the last element 
    if the number match increment the counter value by 1 and if the value doesn't match then reset the counter value to 1 again

    check if the counter value is less than 2 if the counter value is less than 2 than insert into the k list and return the len k

'''

def removeDuplicatesII(nums:list)->int:
    k = 1
    counter = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            counter += 1
        else:
            counter = 1

        if counter <= 2:
            nums[k] = nums[i]
            k += 1
    print(nums[:k])
    return k

nums = [0,0,1,1,1,1,2,3,3]

result = removeDuplicatesII(nums)
print(result)