#!/bin/python3
import sys
import heapq


sizeT = 0
curr = None
oldCurr = None
lowHeap, highHeap = [], []


def addRunningElement(element):
    global curr, lowHeap, highHeap

    if curr == None:
        curr = element
        return
    if element < curr:
        lowHeap.append(element)
        if element > lowHeap[0]:
            heapq._heapify_max(lowHeap)
        return
    highHeap.append(element)
    if element < highHeap[0]:
        heapq.heapify(highHeap)
    return


def balanceAll():
    global curr, lowHeap, highHeap

    if len(lowHeap) - len(highHeap) == 2:
        highHeap.append(curr)
        curr = lowHeap[0]
        del lowHeap[0]
        heapq._heapify_max(lowHeap)
    elif len(highHeap) - len(lowHeap) == 2:
        lowHeap.append(curr)
        curr = highHeap[0]
        del highHeap[0]
        heapq.heapify(highHeap)
    return


def printMedian(size, element):
    global curr, lowHeap, highHeap

    if size == 1:
        print(float(curr))
        return

    if size % 2 == 1:
        print(float(curr))
    else:
        median = None
        if element > oldCurr:
            median = curr + highHeap[0]
            median /= 2.0
        else:
            median = curr + lowHeap[0]
            median /= 2.0
        print(median)
    return


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

    addRunningElement(a_t)
    balanceAll()

    sizeT += 1
    printMedian(sizeT, a_t)
    oldCurr = curr
