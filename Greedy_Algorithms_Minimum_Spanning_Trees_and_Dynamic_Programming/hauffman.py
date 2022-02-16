import heapq
import sys
sys.setrecursionlimit(2000)


def read_file1(name):
    char = list()
    with open(name, 'r') as f:
        for i, line in enumerate(f.readlines()[1:]):
            line = int(line.strip('\n'))
            heapq.heappush(char, (line, str(i)))
    f.close()

    return char


def Huffman(graph):

    if len(graph) == 2:
        new_graph = graph
    else:
        node1 = heapq.heappop(graph)
        node2 = heapq.heappop(graph)
        new_node = (node1[0]+node2[0], node1[1]+'_' + node2[1])
        
        for i in new_node[1].split('_'):            
            length[i] = length.get(i,1)+ 1              
        
        heapq.heappush(graph, new_node)
        Huffman(graph)

    return


def read_file2(name):
    data = list()
    with open(name, 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip('\n')
            data.append(int(line))

    return data


def MWIS(ls):
    IS = [0]*1000    
    IS[0] = ls[0]
    IS[1] = ls[1] if ls[1] >= ls[0] else ls[0]

    for i in range(2,1000):
        if IS[i-2]+ ls[i] > IS[i-1]:
            IS[i] = IS[i-2]+ ls[i]
        else:
            IS[i] = IS[i-1]
#    print(IS)
    
    InSet = list()
    while i>=1:
        if IS[i] == IS[i-1]:
            i -= 1
        else:
            InSet.append(i+1)
            i -= 2
    InSet.append(1)
    
    return InSet


def main():
    char = read_file1('huffman.txt')
    Huffman(char)
    print(max(length.values()))
    print(min(length.values()))

    data = read_file2('mwis.txt')
    s = MWIS(data)

    l = [1, 2, 3, 4, 17, 117, 517, 997]
    for i in l:
        if i in s:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    length = dict()
    main()

