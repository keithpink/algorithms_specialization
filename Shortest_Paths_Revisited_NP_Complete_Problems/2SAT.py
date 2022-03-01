
from functools import reduce
import random
import math

def read_file(name):
    """Given the path/name of the file,
       return the graph (list).
    """
    graph = list()   
    with open(name,'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            line = [int(x) for x in line.split(' ')]
            graph.append(line)                        
    f.close()

    return graph


def reduce_graph(graph):
    '''Given the graph, remove the clause 
       which literals only appears once
    '''
    for i in range(200):
        # print(len(graph))
        pos, neg = dict(), dict()
        re_graph = list()
        
        for cl in graph:
            for x in cl: 
                if x > 0: pos[x] = pos.get(x, 0) +1
                else: neg[-x] = neg.get(-x, 0) +1
   
        for cl in graph:
            if (abs(cl[0]) in pos) and (abs(cl[0]) in neg) and \
            (abs(cl[1]) in pos) and (abs(cl[1]) in neg):
                re_graph.append(cl)
        
        del graph, pos, neg
        graph = re_graph
    
    return graph


def TwoSAT(graph, values):
    '''Given the graph and the assignment,
       determine if the assignment satisfy the graph
    '''
    value_ls = list()
    flip = set()
    for cl in graph:
        v1 = values[abs(cl[0])] if cl[0]>0 else not values[abs(cl[0])]
        v2 = values[abs(cl[1])] if cl[1]>0 else not values[abs(cl[1])]
        # print(v1,v2, (v1 or v2))
        value_ls.append((v1 or v2))
         
        if not (v1 or v2):    # find the clause fail
            flip.update({cl[0],cl[1]})
#     print(values)
#     print(value_ls)
#     print(reduce(lambda x,y: x and y, value_ls))
        
    return reduce(lambda x,y: x and y, value_ls), flip
    

def PA(graph):
    '''Given the graph, repeatedly compute the assignment
    '''
    values = dict()
    for cl in graph:
        for x in cl:
            values[abs(x)] = 0
    N = len(values)
    
    for i in range(round(math.log(N,2))):
        for key in values:       # set initial value
            values[key] = random.choice((True, False))
            
        for j in range(2*(N**2)):  # random walk
            flag, flip = TwoSAT(graph, values)
            if flag:
                return 1
            else:
                k = random.choice(list(flip))
                values[abs(k)] = not values[abs(k)]
                del flip
    return 0


def main():
    files = ['2sat1.txt', '2sat2.txt', '2sat3.txt','2sat4.txt', '2sat5.txt', '2sat6.txt']
    
    for file in files:
        file = 'SAT_data/' + file
        g = read_file(file)
        g = reduce_graph(g)
        print(file, PA(g))
        del g


if __name__ == '__main__':
    main()