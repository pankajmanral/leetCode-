'''

here,
    the logic here is to compare the two elements 
    if the two elements are same then just increment the i but if not then push the non matching element inside the k array and print k
    nums[:k]

    insert the last element inside the array -> nums[k] = nums[-1]
                                                k += 1

'''

def removeDuplicates(nums:list) -> int:
    k = []
    # for i in range(len(nums)-1):
    #     if nums[i] != nums[i+1]:
    #         nums[k] = nums[i]
    #         k += 1
    # nums[k] = nums[-1]
    # k+=1
    # print(nums[:k])
    # return k
    
    for i in nums:
        if i not in k:
            k.append(i)

    print(k)
    return len(k)

nums = [0,0,1,1,1,2,2,3,3,4]

result = removeDuplicates(nums)

print(result)