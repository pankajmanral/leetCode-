def merge_sort(arr:list):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_sorted = merge_sort(left_arr)
        right_sorted = merge_sort(right_arr)

        return merge(left_sorted,right_sorted)
    
def merge(left:list,right:list):
    sorted = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i]) 
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1
    
    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted

nums = [4,6,5,8,3,1,2]
sorted_nums = merge_sort(nums)
print(sorted_nums)