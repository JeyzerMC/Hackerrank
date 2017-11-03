def number_needed(a, b):
    inBoth, b1 = [], list(b)
    for char in a:
        if char in b1:
            b1.remove(char)
            inBoth.append(char)
            
    return len(a) + len(b) - 2*len(inBoth)

a = input().strip()
b = input().strip()

print(number_needed(a, b))