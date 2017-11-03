from collections import defaultdict

def add(rep, contact):
    for token in range(len(contact)):
        rep[contact[:token+1]].append(contact) 
    return

def find(rep, contact):
    print(len(rep[contact]))
    return


rep = defaultdict(list)
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        add(rep, contact)
    elif op == "find":
        find(rep, contact)
