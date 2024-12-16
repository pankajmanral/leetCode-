'''

here,
    we have given the string in roman represetation and we have to reperesent it in noraml interger values
    the rules are :
        if the string is before a biiger value string:
            C -> 100 and M -> 1000
            if C comes before M:
                so the value of C would be considered as minus value not a plus value 
            
            so C is now -100 

'''

def romanToInteger(s:str) -> int:
    romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for index in range(len(s)):
        if index + 1 < len(s) and romanDict[s[index]] < romanDict[s[index + 1]]:
            total -= romanDict[s[index]]
        else:
            total += romanDict[s[index]]
    
    print(total)

s = 'CMXCVIII'
romanToInteger(s)