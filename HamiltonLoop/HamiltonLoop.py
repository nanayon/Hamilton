from adjSet import adjSet as Graph

class HamiltonLoop:
    def __init__(self, G):
        self._G = G
        self._visited = [False] * (G.V + 1)
        self._pre = [1] * (G.V + 1)
        self._end = 0
        self._stv = 1                       #开始结点
        self._std = G.degree(self._stv)     #开始结点的度数
        self.cycle = self._std              #检测周期
        
        self._dfs(self._stv, self._stv, 0, 0)
    
       
    def _dfs(self, v, parent, pathlen, count):
        self._visited[v] = True
        # print("%d's parent is %d" %(v, parent))
        self._pre[v] = parent
        pathlen += 1
        print("%s:%d" %('pathlen', pathlen))

        if pathlen == self._G.V and self._G.has_edge(v, self._stv):
            self._end = v
            return True
        
        for w in self._G.adj(v):
            if not self._visited[w]:
                print("%s:%d" %('当前加入的结点是', w))
                #if ((pathlen) % self.cycle == 0):
                flag, count = self._judge(w, v, count, pathlen)
                if flag:    # 执行剪枝
                    continue 
                    #return False
                print("%s:%d" %('当前count值是', count))

                if self._dfs(w, v, pathlen, count):
                    return True
        
        self._visited[v] = False
        
        return False
    
    #判断当前路径是否有初始点的邻居结点
    def _judge(self, v, parent, count, pathlen):
        temp = count
        #检测当前结点
        if(v in self._G._adj[self._stv]):
            count += 1
            print("%s:%d, %s:%d" %('v', v, 'count', count))
        
        '''    
        #检测之前结点
        v = parent
        for i in range(self.cycle):
            if(v in self._G._adj[self._stv]):
                count += 1
                print("%s:%d, %s:%d" %('v', v, 'count', count))
            v = self._pre[v]    #这时候parent还没有录入
        '''
            
        if count == self._std and pathlen != self._G.V - 1:
            print("剪枝")
            return True, temp
        
        return False, count
    
    #根据充分或必要条件判断
    #储存答案，如果有更好的答案，则替换当前答案
    
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
    
   
        
if __name__ == '__main__':
    filename = '../g2.txt'
    graph = Graph(filename)
    hamilton_loop = HamiltonLoop(graph)
    print(hamilton_loop.result())