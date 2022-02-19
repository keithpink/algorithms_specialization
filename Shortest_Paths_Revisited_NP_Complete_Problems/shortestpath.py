
import numpy as np
vertices = 1000

def read_file(name):
    global vertices

    g = dict()
    re_g = dict()
    cost = dict()
    for i in range(1,vertices+1):
        g[i] = list()
        re_g[i] = list()

    with open(name, 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            line = [int(x) for x in line.split(' ')]
            
            g[line[0]].append(line[1])
            re_g[line[1]].append(line[0])
            cost[(line[0], line[1])] = line[2]
        f.close()
    
    return g, re_g, cost


def BF(graph, re_graph, cost):
    global vertices
    global edges
    
    dist = np.zeros((vertices+1, 2),int)   # 初始化最短距离
    graph[0] = list()
    for x in range(1, vertices+1):            #   构建虚拟点
        graph[0].append(x)    
        cost[(0,x)] = 0
       
    # print(i,dist)
    for i in range(1, vertices+5):
        dist[:,0] = dist[:,1]
        for v in range(1, vertices+1):
            if len(re_graph[v]) == 0:
                continue
            else:
                path =  min( (dist[w,0]+cost[(w,v)]) for w in re_graph[v] )    
                dist[v,1] = min(dist[v,0], path)                           
        
        if (dist[:,0] == dist[:,1]).all():    # 循环提前终止条件
            break         
            
         
    if (dist[:,0] == dist[:,1]).all():    # 看有没有负环
        return np.min(dist)
    else:
        return None


def main():
    for f in ['g1.txt','g2.txt','g3.txt']:
        g, re_g, cost = read_file(f)
        print(BF(g,re_g, cost))

if __name__ == "__main__":
    main()
