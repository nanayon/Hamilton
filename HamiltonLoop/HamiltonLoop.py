from adjSet import adjSet as Graph

class HamiltonLoop:
    def __init__(self, G):
        self.fo = open("output.txt", "w")
        self._G, self.subG = G
        self._visited = [False] * (G.V + 1)
        self._pre = [1] * (G.V + 1)
        self._end = 0
        self._stv = 1                       #开始结点
        self._std = G.degree(self._stv)     #开始结点的度数
        self.cycle = self._std              #检测周期
        self.maxlen = int(self._G.V * 0.8)  #记录最大长度
        self.back = 0                       #回溯的次数
        self._dfs(self._stv, self._stv, 0, 0)
    
       
    def _dfs(self, v, parent, pathlen, count):
        
        self._visited[v] = True
        # print("%d's parent is %d" %(v, parent))
        self._pre[v] = parent
                
        pathlen += 1
        if pathlen > self.maxlen:
            self.maxlen = pathlen
            print(self.maxlen)
        print("%s:%d" %('pathlen', pathlen), file = self.fo)
        #print("%s:%d" %('pathlen', pathlen))

        if pathlen == self._G.V and self._G.has_edge(v, self._stv):
            self._end = v
            return True
        
        for w in self._G.adj(v):
            if not self._visited[w]:
                print("%s:%d" %('当前加入的结点是', w), file = self.fo)
                '''
                if (pathlen) % self.cycle == 0:
                    self.back, count = self._judge(w, v, count, pathlen)
                if self.back:   # 执行剪枝,backc为剪枝的次数
                    self.back = self.back - 1
                    continue    # 这里回溯应该多回一些，应该回到上一个被检测出的顶点的前一个顶点
                        #print("%s:%d" %('当前count值是', count))
                self.back = 0
                '''
                if self._dfs(w, v, pathlen, count):
                    return True
        
        self._visited[v] = False

        return False
        
    #判断当前路径是否有初始点的邻居结点
    def _judge(self, v, parent, count, pathlen):
        temp = count
        tempf1, tempf2 = False, False
        #tempv = v
        #检测当前结点
        backc = 1
        backc2 = 0
        if(v in self._G._adj[self._stv]):
            count += 1
            print("%s:%d, %s:%d" %('v', v, 'count', count), file = self.fo)
            tempf1 = True
        
        #检测之前结点
        v = parent
        for i in range(self.cycle - 1):
            backc = backc + 1
            if(v in self._G._adj[self._stv]):
                count += 1
                print("%s:%d, %s:%d" %('v', v, 'count', count), file = self.fo)
                if tempf2 == False:
                    backc2 = backc
                    tempf2 = True
                #    tempf = False
                #    tempv = v   #记录路径上的点，以便于回溯到此处
            v = self._pre[v]    #这时候parent还没有录入
            
        if tempf1 == True:
            backc = 1
        elif tempf2 == True:
                backc = backc2
            
        if count >= self._std and pathlen != self._G.V - 1:
            print("剪枝", file = self.fo)
            return backc, temp   #回溯到tempv的前一个点 回溯的次数，count值
        
        return 0, count   #0代表不剪枝，非零才剪枝
    '''
    #得到未访问部分的子图
    def get_subgraph(self, visited):
        for v in visited:
            self.subG.remove_vertex(v)
        return self.subG._adj
    
    #得到化简后的子图
    def simp_subgraph(self, rest):
        c = 0
        for v in rest:
            if self.subG.degree(v) == 2:
                for w in self.subG.adj(v):         #不能有出点
                    if self.subG.degree(v) == 2:
                        self.subG.remove_vertex(w) #合并这两个结点
                    else:
                        #收缩三角形

    #根据充分或必要条件判断
    #储存答案，如果有更好的答案，则替换当前答案
    '''
    def result(self):
        res = []
        if self._end == 0:
            return res
        
        curr = self._end
        while curr != self._stv:
            res.append(curr)
            curr = self._pre[curr]
        res.append(self._stv)
        
        return res[::-1]
            
    def __del__(self):
        self.fo.close()
    
   
        
if __name__ == '__main__':
    filename = '../g2.txt'
    graph = Graph(filename)
    hamilton_loop = HamiltonLoop(graph)
    print(hamilton_loop.result())
    