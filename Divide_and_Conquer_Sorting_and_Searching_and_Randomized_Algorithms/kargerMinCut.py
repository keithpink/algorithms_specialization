import random
def count(graph):        # input is a list    
    if len(graph) == 2:
        mincut =  len( graph[ list(graph.keys())[0]]   )
        return mincut
    else:
        v = random.choice(list(graph.keys()))    # cut the edge starting from v
        u = random.choice(graph[v])               # cut the edge ending with u
        new_graph = contract(graph, v, u)
        mincut = count( new_graph )                   # recursive call
    return mincut


def contract(graph, v, u):
    for node in graph[u]:
        if node != v:
            graph[v].append(node)        # merge edges starting with u to v
        graph[node].remove(u)            # delete edges starting with u
        
        if node != v:
            graph[node].append(v)        # reconstruct edges between v and other nodes    
    
    del graph[u]
    return graph


def read_file(name):
    data = []
    with open(name,"r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            line = line.strip()
            data.append(line)        

    graph = dict()
    for x in data:
        x = x.split('\t')
        graph[int(x[0])] = [ int(n) for n in x[1:]]
    
    return graph


import copy
def main():
    graph = read_file('kargerMinCut.txt')
    cuts = list()
    for i in range(20):
        g = copy.deepcopy(graph)
        cuts.append(count(g))
    return min(cuts)
    

if __name__ == '__main__':
    print(main())