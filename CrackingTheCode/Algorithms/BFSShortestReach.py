import queue
from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(list)

    def connect(self, initial, final):
        self.edges[initial].append(final)
        self.edges[final].append(initial)
        return
    
    def find_all_distances(self, root):
        self.edges[root]
        visited = {}
        distance = [0 for x in range(self.nodes)]
        myQ = queue.Queue()

        myQ.put((root, root))
        visited[root] = True

        while not myQ.empty():
            startIn, node = myQ.get()
            for adj in self.edges[node]:
                if adj not in visited:
                    distance[adj] = distance[node] + 6
                    visited[adj] = True
                    myQ.put((node, adj))
        
        strQuerr = ""
        for node in range(self.nodes):
            if node != root:
                if distance[node] != 0:
                    strQuerr += str(distance[node]) + " "
                else:
                    strQuerr += "-1 "

        print(strQuerr.strip())
        return


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)