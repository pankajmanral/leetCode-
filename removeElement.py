'''

here,
    in the commented out approach the solution is rejected in leetcode because the output uses extra space the question mentioned that to 
    solve the question in place 

    the second commeted code the solution is again correct but leetcode also expect the list with the remove element 

'''

def removeElement(nums:list,val:int) -> list:
    # k = []
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         k.append(nums[i])
    # return k

    # k = 0
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         k += 1
    # return len(k)

    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3,2,2,3]
val = 3

result = removeElement(nums,val)
print(result)