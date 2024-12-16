'''

here,

    * empty list are considered Falsy *

    stack = []
    if not stack:
        print("Empty stack")
    elif stack:
        print("Not empty)

    we have to check if the brackets are correctly closing or not in correct order
    loop through the given string check if the string gives a opening or a closing bracket 
    if its a opeing bracket append the bracket(string) into the stack and move 
    but if its a closing bracket the pop the latest element appended into the stack(list)

'''

def validParenthesis(s:str) -> bool:
    brackets = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:  
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                print(False)
                break
    else:
        print(not stack)


s = ')'
validParenthesis(s)