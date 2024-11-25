''' 

here :
    the 0's in the nums1 list represent the empty spaces that have to be filled with the nums from the second list in sorted order
    p1,p2 are the last number in the respective list that should be compared
    we get the last number by m and n respectively 
    index is the position where the elements have to be placed in the bigger list (first one) in desc order

    if n1 > n2 :
        the bigger number will be added in the end of the first list i.e in the position of the 0
    
'''
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

# output -> [1,2,2,3,5,6]

def mergeArray(nums1,nums2,m,n)->list:
    p1 = m-1
    p2 = n-1
    index = len(nums1)-1

    while p1 >= 0 and p2 >= 0:
        n1 = nums1[p1]
        n2 = nums2[p2]

        if n1 > n2:
            nums1[index] = n1
            p1 -= 1
        else:
            nums1[index] = n2
            p2 -= 1
        index -= 1

    while p2 >= 0:
        nums1[index] = nums2[p2]
        p2 -= 1
        index -= 1

    print(nums1)

mergeArray(nums1,nums2,m,n)