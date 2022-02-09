def read_file(name):
    graph = dict()
    with open('dijkstraData.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            
            if line:
                key = int(line[0])
                graph[key] = list()
                for edge in line[1:-1]:    # 最后一个元素是制表符，需要舍去
                    edge = edge.split(',')
                    edge = [int(x) for x in edge]
                    graph[key].append(edge)
    return graph


def ShortPath(graph,dist,t, A):
    while not t in A:
        p = 0   # 候补点
        d = 1000000 #  候补距离
        for node in A:
            for edge in graph[node]:
                if not edge[0] in A:
                    x = dist[node] + edge[1]
                    if  x < d:              # 比较得出最短的路径
                        p = edge[0]
                        d = x
        dist[p] = d        # 将最短的路径存入字典
        A.append(p)

    print(dist[t])


def main():
    dist = dict()
    s = 1           # source node
    t = 5      # terminate

    A = [s]          # nodes processed
    dist[s] = 0  # distance dictitionary
    terminate = [7,37,59,82,99,115,133,165,188,197]
    ans = []
    graph = read_file('dijkstraData.txt')
    for t in terminate:
        di = ShortPath(graph, dist, t, A)
        ans.append(di)


if __name__ == '__main__':
    main()


