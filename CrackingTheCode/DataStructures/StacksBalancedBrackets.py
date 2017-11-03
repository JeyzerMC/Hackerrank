def is_matched(expression):
    myDict = {')':'(', '}':'{', ']':'['}
    myStack = []
    for token in expression:
        if token in '([{':
            myStack.append(token)
        elif len(myStack) == 0 or myDict[token] is not myStack.pop():
                return False
    return len(myStack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
