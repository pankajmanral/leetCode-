'''

here, 
    first initailize an empty dict to count the appearance of each number 
    then create the list of the count of the apperance(values of the dict)
    create a set of the that list so that if there are duplicate values or repeated value they can be eliminated

    finally if the lenght of the list and the set is same return True else return False

'''

def uniqueOccurances(arr:list) -> bool:
    # initialize an empty dict to store the appearance of each value/number
    count = {}

    for val in arr:
        if val not in count:
            count[val] = 1
        else:
            count[val] += 1

    occurances = list(count.values())
    seenset = set(occurances)

    if len(occurances) != len(seenset):
        return False
    else:
        return True

arr = [1,1,1,2,2,3]
print(uniqueOccurances(arr))