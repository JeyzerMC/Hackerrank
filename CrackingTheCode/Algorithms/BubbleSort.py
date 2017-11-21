n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

nbSwapTotal = 0
for i in range(len(a)):
    nbSwap = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            nbSwap += 1
    if nbSwap == 0:
        break
    nbSwapTotal+= nbSwap

print("Array is sorted in {0} swaps.".format(nbSwapTotal))
print("First Element:", a[0])
print("Last Element:", a[len(a)-1])