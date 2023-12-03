#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, n):
    color = [0] * n
    def isSafe(node,c):
        for i in range(n):
            if graph[node][i] == 1 and color[i] == c:
                return False
        return True
    #your code here
    def recursive(node):
        if node == n:
            return True
        for c in range(1,m+1):
            if isSafe(node, c):
                color[node] = c
                if recursive(node+1):
                    return True
                color[node] = 0
        return False
    
    return 1 if recursive(0) else 0
