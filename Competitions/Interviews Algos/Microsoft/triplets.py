def nbTriplets(n, arr):
    arr, nbOcc = sorted(arr), 0
    for i in range(len(arr)):
        if i > n:
            break
        for j in range(i+1, len(arr)):
            if i + j > n:
                break
            for k in range(j+1, len(arr)):
                if i + j + k > n:
                    break
                nbOcc += 1
    return nbOcc


n = int(input())
arr = list(map(int, input().split(' ')))

print(nbTriplets(n, arr))