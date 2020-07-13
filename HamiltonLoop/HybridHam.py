from adjSet import adjSet as Graph
from goto import with_goto
import sys

class HybridHam:
    def __init__(self, G):
        self.fo = open("output.txt", "w")
        self.__G = G
        self.__visited = [False] * (G.V + 1)
        self.__pre_visted = [False] * (G.V + 1)
        # self.preprocessor()
        # self.delete_edge()
        self.detection1()
        self.__record = [0] * (G.V + 1)
        self.__list_v = self.__sort_degree()
        self.__stv = 4
        print(self.__stv)
        self.__path = []
        self.__greedy(self.__stv)
    
    """处理度为3的三角形"""
    @with_goto
    def preprocessor(self): 
        count = 0
        for w in range(1, self.__G.V+1):
            label .restart
            #print("'%d'" %(w))
            list_v = []
            if self.__G.degree(w) == 3:
                 for u in self.__G.adj(w):
                     if self.__G.degree(u) == 3:
                         list_v.append(u)
                 if len(list_v) >= 2:
                     list_v2 = []
                     for i in range(0, len(list_v)):
                         for j in range(i, len(list_v)):
                             if self.__G.has_edge(list_v[i], list_v[j]):
                                 list_v2.append(list_v[i])
                                 list_v2.append(list_v[j])
                                 #print(self.__G.adj(w))
                                 self.__G.merge_vertex(w, list_v2)
                                 #print(self.__G.adj(w))
                                 count += 1
                                 goto .restart
        print(count)
    
    #删除度为2的点的邻接点之间直接相连的边, 错误概率：较低
    def delete_edge(self):
        count = 0
        for w in range(1, self.__G.V+1):
            if self.__G.degree(w) == 2:
                templist = list(self.__G.adj(w))
                if self.__G.has_edge(templist[0], templist[1]):
                    print(templist)
                    self.__G.remove_edge(templist[0], templist[1])
                    count += 1
        print("发现一定可以删除的边的条数：%d" %count)
    
    # 处理度为2的点
    @with_goto
    def detection(self): 
        #先处理连边
        #self.delete_edge()
        #接下来是收缩操作
        count = 0
        for w in range(1, self.__G.V+1):
            label .restart
            if self.__G.degree(w) == 2:
                count += 1
                for u in self.__G.adj(w):
                    if self.__G.degree(u) == 2:
                        self.__G.merge_vertex(w, [u])
                        count += 1
                        goto .restart
        print("处理的度为2的顶点个数：%d" %count)

    # 处理度为2的点的第二种情况 
    def detection1(self):
        count = 0
        for w in range(1, self.__G.V):
            if self.__G.degree(w) == 2:
                templist = list(self.__G.adj(w))
                if self.__G.degree(templist[0]) == 3 and self.__G.degree(templist[1]) == 3:
                    if len(self.__G.adj(templist[0]) & self.__G.adj(templist[1])) > 1:
                        self.__G.merge_vertex(w, templist)
                        count = count + 1
        print("处理情况2中, 度为2的顶点个数：%d" %count)
    
    # 处理五个结点的缩减，不完整
    @with_goto       
    def detection2(self):
        count = 0
        for w in range(1, self.__G.V):
            templist = []
            if self.__G.degree(w) == 3:
                for u in self.__G.adj(w):
                    if self.__G.degree(u) == 3 or self.__G.degree(u) == 4:
                        templist.append(u)
                    for i in range(0, len(templist)):
                        for j in range(i, len(templist)):
                            if self.__G.adj(i)-{j} == self.__G.adj(j)-{i}:
                                list_v = list(self.__G.adj(i)|self.__G.adj(j)|{i, j}-{w})
                                self.__G.merge_vertex(w, list_v)
                                count += 1
        print("处理情况2中, 度为2的顶点个数：%d" %count)
    
    """按顶点的度数从大到小排序"""
    def __sort_degree(self):
        dic = {}
        for i in range(1, self.__G.V):
            dic[i] = self.__G.degree(i)
        list_v = sorted(dic.items(), key = lambda kv:kv[1], reverse = True)
            
        return list_v
    
    """贪心搜索"""
    def __greedy(self, v):
        
        self.__visited[v] = True
        if v not in self.__path:
            self.__path.append(v)
        
        if len(self.__path) == self.__G.V and self.__path[-1] in self.__G.adj(self.__path[0]):
            print("已找到哈密尔顿圈")
            return True
        
        end = True
        for w in self.__G.adj(v):
            if not self.__visited[w]:   #如果还存在没有访问过的
                end = False
                break
        if end:
            self.__record[v] = self.__record[v] + 1     # 作为不可扩展的尾端结点，record+1
            #print(v)
            #print(self.__record[v])
            return False
        
        #要改
        for w in self.__G.adj(v):
            if not self.__visited[w]:
                next_v = w
        #print(self.__G.adj(v), file = self.fo)
        
        for w in self.__G.adj(v):    
            if not self.__visited[w]:
                #如果不是不可到达的顶点
                #if not self.__unreachable(w):
                    #选择领域中度最小的点加入路径
                if self.__G.degree(w) < self.__G.degree(next_v):
                    next_v = w
        if self.__greedy(next_v):
            return True

        if len(self.__path) != self.__G.V or self.__path[-1] not in self.__G.adj(self.__path[0]):
            self.__rotation_trans()
        
        return False
    
    def __find_stv(self):
        max_degree = 1
        max_v = 1
        for i in range(1, self.__G.V):
            if self.__G.degree(i) > max_degree:
                max_degree = self.__G.degree(i)
                max_v = i
        return max_v
                
    """检测不可达顶点"""
    def __unreachable(self, v):
        for w in self.__G.adj(v):
            if not self.__visited[w]:
                return False
        return True
    
    '''旋转变换'''
    def __rotation_trans(self):  #进行变换的端点
        #print(self.__path)
        next_v_list = []
        for w in self.__G.adj(self.__path[-1]):
            if self.__visited[w]:
                if len(self.__path)-1 - self.__path.index(w) != 1:   #可以与起点连接，这里需不需要检测不可达？
                    next_v_list.append(w)
        # print(next_v_list)
        # 还要检查一下是否能进行旋转变换
        # 转置
        if not next_v_list:
            #print("在第二阶段退出")
            return False
        
        next_v = 0
        #选具体的端点,选出一个就好 这个应该叫end啦
        #如果有可到达的端点，直接选这个可到达的，否则选record次数最小的
        for w in next_v_list:   
            i = self.__path.index(w) + 1                    #现在是尾端点节点候选，就是当前w在path中的邻居结点
            if not self.__unreachable(self.__path[i]):      #检测新的尾端点是否可到达，检测到可达顶点就跳出
                next_v = self.__path[i]
                break
            
        # 如果没有可达顶点
        # 那么就只好将不可达的顶点作为结束顶点，然后祈祷一下，在经过为数不多的转置后能够重新出现可达顶点   
        if not next_v:
            #print("没有找到可以到达的顶点")
            min_record = 100
            min_v = 0
            for w in next_v_list:   #应该是检测在path中w的邻居结点
                i = self.__path.index(w)+1
                if self.__record[self.__path[i]] < min_record:
                    min_record = self.__record[self.__path[i]]
                    min_v = self.__path[i]
                    #print("%s=%d, %s%d%s:%d" %('min_v', min_v, 'record[',self.__path[i],']',self.__record[self.__path[i]]))
            next_v = min_v
            if min_record >= 3:
               next_v = self.__path[0] #stv

        
        #print(next_v)
        #self.__record[next_v] = self.__record[next_v] + 1
        
        i = self.__path.index(next_v)    #现在是尾端点节点候选
        #print(i)
        j = len(self.__path) - 1   
        #print(j)                     #防止抖动,加数组的话，这里也有一种陷入死循环的可能
        while(i < j):
            temp = self.__path[i] 
            self.__path[i] = self.__path[j]
            self.__path[j] = temp
            i = i + 1
            j = j - 1
        #print(self.__path)
        if self.__greedy(self.__path[-1]):
            return True
        
    def is_hamilton(self, path):
        i = 0
        end = True
        if len(path) != self.__G.V:
            end = False
        while(i < len(path)-1):
            if not self.__G.has_edge(path[i], path[i+1]):
                print("%d-X-%d" %(path[i], path[i+1]))
                end = False
            i = i + 1
        if end:
           if self.__G.has_edge(path[0],path[-1]):
               print("成功了！")
           else:
               print("只能找到哈密尔顿路径")
        return end
            
    '''旋转变换'''
    def __rotation(self):
        v = 0
        max_degree = 0
        for w in self.__G.adj(self.__path[-1]):
            if self.__visited[w]:
                if self.__G.V - self.__path.index(w) != 1:   #这里需不需要检测不可达？
                    if self.__G.degree(w) > max_degree:
                        max_degree = self.__G.degree(w)
                        v = w
        # 还要检查一下是否能进行旋转变换
        # 转置     
        if v == 0:
            print("在第二阶段退出")
            return False
        
        i = self.__path.index(v)+1
        j = self.__G.V
        while(i < j):
            temp = self.__path[i] 
            self.__path[i] = self.__path[j]
            self.__path[j] = temp
            i = i + 1
            j = j - 1
        
        self.__greedy(v)
        
    def result(self):
        print(self.__path)
        print(len(self.__path))
        self.is_hamilton(self.__path)
        
    def __str__(self):
        return '111'
        
    def __repr__(self):
        return '111'

        
if __name__ == '__main__':
    # sys.setrecursionlimit(5000)
    filename = '../g7.txt'
    graph = Graph(filename)
    hamilton_loop = HybridHam(graph)
    hamilton_loop.result()
