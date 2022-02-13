from operator import itemgetter, attrgetter

def read_file1(name):
    ''' run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length).
    '''
    data = list()
    with open(name, 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip('\n')
            line = line.split(' ')
            w = int(line[0])
            l = int(line[1])
            diff = w - l
            data.append(tuple([-w,l,-diff]))
    f.close()

    return data


def read_file2(name):
    ''' run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length)
    '''
    data = list()
    with open(name, 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip('\n')
            line = line.split(' ')
            w = int(line[0])
            l = int(line[1])
            r = w/l
            data.append(tuple([-w,l,-r]))
    f.close()

    return data


def CompTime(data):
    data = sorted(data, key=itemgetter(2,0,1))
#     print(data)
    time_sum = 0
    comp_time = 0
    for t in data:
        comp_time += t[1]
        time_sum += (-t[0])*comp_time
#         print(comp_time)
#         print(time_sum)
    print(time_sum)


def read_file3(name):
    ''' minimum spanning tree
    '''
    cost = dict()
    graph = dict()
    for i in range(500):
        graph[i+1] = list()

    with open("edges.txt", 'r') as f:
        for line in f.readlines()[1:]:
            line = line.strip('\n')
            line = line.split(' ')
            line = [int(x) for x in line]
    #         print(line)
            
            graph[line[0]].append(line[1])
            graph[line[1]].append(line[0])

            cost[(line[0],line[1])] = line[2]
            cost[(line[1],line[0])] = line[2]
    f.close()

    return graph, cost


def Prim(graph, cost):
    '''Prim's minimum spanning tree algorithm
    '''
    processed = [1]
    total_cost = 0
    
    while len(processed) < len(graph.keys()):
        mincost = float('inf')
        for v in processed:
            for u in graph[v]:
                if u not in processed:
                    if cost[(v,u)] < mincost:
                        mincost = cost[(v,u)]
                        min_node = u  
        total_cost += mincost
        processed.append(min_node)
#         print(processed)
       
    print(total_cost)


def main():
    data1 = read_file1('jobs.txt')
    CompTime(data1)
    data2 = read_file2('jobs.txt')
    CompTime(data2)
    graph, cost = read_file3('edges.txt')
    Prim(graph, cost)


if __name__ == "__main__":
    main()