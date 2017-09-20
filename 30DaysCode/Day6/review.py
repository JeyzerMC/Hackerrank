n = int(input())


for i in range(n):
    s = input()
    a = ""
    b = ""
    for i in range(len(s)):
        if i%2 == 0:
            a += s[i]
        else:
            b += s[i]
    print("{0} {1}".format(a, b))
