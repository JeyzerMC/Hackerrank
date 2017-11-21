def iceCreamParlor(money, n, arr):
    for iter1 in range(n):
        for iter2 in range(n):
            if iter1 != iter2:
                if arr[iter1] + arr[iter2] == money:
                    return iter1 + 1, iter2 + 1
    return None, None

def iceCreamParlorON(money, n, arr):
    myMap = {}
    for it in range(n):
        if money - arr[it] in myMap:
            return myMap[money - arr[it]], it + 1
        myMap[arr[it]] = it + 1
    return None, None


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # print(*iceCreamParlor(m, n, a))
    print(*iceCreamParlorON(m, n, a))