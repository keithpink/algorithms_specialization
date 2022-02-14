from unionfind import unionfind
from operator import itemgetter
from functools import reduce
from networkx.utils.union_find import UnionFind
from itertools import combinations


def read_file(name):
    graph = list()
    with open(name) as f:
        for line in f.readlines()[1:]:
            line = line.strip('\n')
            line = line.split(' ')
            line = tuple([int(x) for x in line])
            graph.append(line)
    f.close()
    return graph


def K_clusters(graph, K):
    union = unionfind(500)
    graph = sorted(graph, key=itemgetter(2))
    while len(union.groups()) > K:
        pair = graph.pop(0)
        if not union.issame(pair[0]-1, pair[1]-1):
            union.unite(pair[0]-1, pair[1]-1)
    
    for edges in graph:
        if not union.issame(edges[0]-1, edges[1]-1):
            dist = edges[2]
            break
    
    return dist


def read_file2(name):
    nodes = list()
    graph = dict()

    with open(name) as f:
        for i,line in enumerate(f.readlines()[1:]):
            line = line.strip('\n')
            line = line.split(' ')
            line = reduce(lambda x,y: x+y, line)
        
            nodes.append(int(line,2))
            graph[int(line,2)] = i+1

        union = UnionFind(graph.values())

    f.close()
    return graph, union


def clustering(graph, union):
    for node in graph:
        for i in range(24):
            neigb1 = node^(1<<i)
            if neigb1 in graph.keys():
                union.union(graph[neigb1], graph[node])
        
        for i,j in combinations(range(24),2):
            neigb2 = node ^(1<<i) ^(1<<j)
            if neigb2 in graph.keys():
                union.union(graph[neigb2], graph[node])

    clusters = list( map(sorted, union.to_sets()))
    return len(clusters)


def main():
    g1 = read_file('clustering1.txt')
    print(K_clusters(g1, 4))
    g2, union = read_file2('clustering2.txt')
    print(clustering(g2, union))

if __name__ == '__main__':
    main()

