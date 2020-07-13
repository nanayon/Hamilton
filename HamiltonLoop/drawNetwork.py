import networkx as nx
import matplotlib.pyplot as plt
from adjSet import adjSet as Graph    

if __name__ == '__main__':
    filename = '../alb1000.hcp'
    graph = Graph(filename)
    
    G = nx.Graph()      #创建无向无环图
    G.add_edges_from(graph.get_all_edge())
    #G.add_edge('1', '5') #添加边
    print(G.number_of_nodes())
    print(G.number_of_edges())

    nx.draw(G, font_size =8, node_size =30)          #图形显示
    # nx.draw(G, pos = nx.random_layout(G), node_color = 'b', edge_color = 'r', with_labels = True, font_size =18, node_size =20)
    plt.savefig("large.png", dpi=5000)

  