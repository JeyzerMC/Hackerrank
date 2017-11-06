from heapq import heappush, heappushpop
import sys

# SOLUTION BY POINT_TO_NULL, adapted

n = int(input().strip())
a = []
a_i = 0
lowHeap = []
highHeap = []
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

    a_t = heappushpop(highHeap, a_t)
    a_t = -heappushpop(lowHeap, -a_t)

    if len(highHeap) <= len(lowHeap):
        heappush(highHeap, a_t)
    else:
        heappush(lowHeap, -a_t)

    if len(highHeap) > len(lowHeap):
        print('%.1f' % highHeap[0])
    else:
        median = highHeap[0] - lowHeap[0]
        median /= 2.0
        print(median)
