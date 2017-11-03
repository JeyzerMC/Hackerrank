from collections import defaultdict
def ransom_note(magazine, ransom):
    magDict = defaultdict(int)
    for token in magazine:
        magDict[token] += 1
        
    for elem in ransom:
        if magDict[elem] == 0:
            return False
        else:
            magDict[elem] -= 1
            
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    