from adjSet import adjSet as Graph

class HamiltonLoop:
    
    def __init__(self, G):
        self._G = G
        self._visited = [False] * (G.V + 1)
        self._pre = [1] * (G.V + 1)
        self._end = 0
        self._dfs(1, 1, G.V)
        
    def _dfs(self, v, parent, left):
        self._visited[v] = True
        self._pre[v] = parent
        left -= 1
        if left == 0 and self._G.has_edge(v, 1):
            self._end = v
            return True
        
        for w in self._G.adj(v):
            if not self._visited[w]:
                if self._dfs(w, v, left):
                    return True
        
        self._visited[v] = False
        
        return False
        
    def result(self):
        res = []
        if self._end == 0:
            return res
        
        curr = self._end
        while curr != 1:
            res.append(curr)
            curr = self._pre[curr]
        res.append(1)
        
        return res[::-1]
    
    def judge(self, v, count):
        w = v
        if(left % 7 == 0)
            for i in range(7):
                if(self._pre[v] in self._G._adj[w])
                    count++
            v = self._pre[v]
        return count
        
if __name__ == '__main__':
    filename = '../g2.txt'
    graph = Graph(filename)
    hamilton_loop = HamiltonLoop(graph)
    print(hamilton_loop.result())