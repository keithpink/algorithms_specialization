import numpy as np
import matplotlib.pyplot as plt


def read_file(name):
	graph = list()
	with open(name, 'r') as f:
	    for line in f.readlines()[1:]:
	        line = line.strip()
	        line = [float(x) for x in line.split(' ')]
	        graph.append(line)
	f.close()

	graph = np.asarray(graph)
	return graph


def plot_graph(graph):
	X = graph[:,0]
	Y = graph[:,1]
	annotation = [str(i) for i in range(len(X))]
	plt.scatter(X,Y)
	for i,label in enumerate(annotation):
	    plt.annotate(label, (X[i], Y[i]))
	plt.show()
	return


def PowerSet(ls):
    N = len(ls)
    S = list()
    Bitmask = dict()
    for i in range(2**N):
        subset = set()
        for j in range(N):
            if (i>>j)%2:
                subset.add(ls[j])
        
        if 0 in subset:        # 只记录包含 1 的子集
            S.append(i)
            Bitmask[i] = subset
    return S, Bitmask


def dist(graph,i,j):
    return np.sqrt( (graph[i,0]-graph[j,0])**2 + (graph[i,1]-graph[j,1])**2 )


def TSP(graph):
    N = len(graph[:,0])
    S, Bitmask = PowerSet(list(range(N)))
    
    # A[i,j] 表示 第2*1+1个子集，到第 j 个终点 
    A = np.zeros((len(S), N), float)
    for i in range(len(S)):
        A[i,0] = 0 if i == 0 else float('inf')    # 出发点只能在开始和结束被访问
    
    for i in S:
        for j in (Bitmask[i]-{0}):
            A[(i-1)//2, j] = min( ( A[((i^(1<<j))-1)//2,k]+dist(graph,k,j)) for k in (Bitmask[i]-{j}) )
            # print(Bitmask[i], j, A[(i-1)//2, j])
            
    return min((A[len(S)-1,j]+dist(graph,j,0)) for j in range(1,N))


def main():
    g =	read_file('tsp.txt')
    plot_graph(g)
    
    cluster1 = g[:13,]
    a1 = TSP(cluster1)
    cluster2 = g[11:,]
    a2 = TSP(cluster2)

    result = a1 + a2 - 2*dist(g,11,12)
    print(result)


if __name__ == '__main__':
	main()



