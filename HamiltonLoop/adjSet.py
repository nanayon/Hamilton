from GraphBase import GraphBase

class adjSet(GraphBase):
    def __init__(self, filename):
        #读取文件
        lines = None
        with open(filename, 'r') as f:
            lines = f.readlines()
        if not lines:
            raise ValueError('Expected something from input file!')
        
        #私有变量lines[0] -> V E
        self._V, self._E = (int(i) for i in lines[0].split())
        if self._V < 0:
            raise ValueError('V must be non-negative')   
        if self._E < 0:
            raise ValueError('E must be non-negative')
        
        #邻接表，记录邻接点
        self.__edgelist = []
        self._adj = [set() for _ in range(self._V+1)]
        for each_line in lines[1:]:
            a, b = (int(i) for i in each_line.split())
            self._validate_vertex(a)
            self._validate_vertex(b)
            if a == b:
                raise ValueError('Self-Loop is detected!')
            if b in self._adj[a]:
                raise ValueError('Paralle edges are detected!')
            self._adj[a].add(b)
            self._adj[b].add(a)
            self.__edgelist.append((a, b))

    @property
    def V(self):
        return self._V
    
    @property
    def E(self):
        return self._E
    
    def get_all_edge(self):
        return self.__edgelist
    
    #判断两顶点间是否有边存在
    def has_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        return w in self._adj[v]
    
    #返回所有邻接结点
    def adj(self, v):
        self._validate_vertex(v)
        return self._adj[v]
        
    def degree(self, v):
        return len(self.adj(v))
    
    #判断
    def _validate_vertex(self, v):
        if v < 0 or v > self._V:
            raise ValueError('vertex ' + v + ' is invalid')
    
    #删除边
    def remove_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        if w in self._adj[v]:
            self._adj[v].remove(w)
        if v in self._adj[w]:
            self._adj[w].remove(v)
    
    #删除点,并删除与所有这个点相邻的边
    def remove_vertex(self, v):
        self._validate_vertex(v)
        for w in list(self._adj[v]):
            self._adj[v].remove(w)
            self._adj[w].remove(v)
    
    #将其他点的边转接到点v上，然后删除list_v中的点
    def merge_vertex(self, v, list_v):
        #print(list_v)
        for w in list_v:
            for u in self._adj[w]:
                if u not in self._adj[v] and u not in list_v and u != v:
                    self._adj[v].add(u)         #向v的邻域添加点
                    self._adj[u].add(v)
            #print(self._adj[v])
            self.remove_vertex(w)               #删除点w和与之关联的边
    
    def __str__(self):
        res = ['V = {}, E = {}'.format(self._V, self._E)]
        for v in range(1, self._V + 1):
            res.append('{}: {}'.format(v, ' '.join(str(w) for w in self._adj[v])))
        return '\n'.join(res)
            
    def __repr__(self):
        return self.__str__()
    
if __name__ == '__main__':
    filename = '../alb1000.hcp'
    adj_list = adjSet(filename)
    print(adj_list)