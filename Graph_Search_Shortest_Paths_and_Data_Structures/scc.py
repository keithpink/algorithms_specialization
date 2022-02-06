data = list()
with open('scc.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        line = line.strip()
        if line:
            data.append(line)

# print(data[:10])

num_nodes = 875714
graph = dict()
re_graph = dict()
for i in range(num_nodes):
    graph[i+1] = [] 
    re_graph[i+1] = []
    
for edge in data:
    edge = edge.split(' ')
    graph[int(edge[0])].append(int(edge[1]))
    re_graph[int(edge[1])].append(int(edge[0]))



order = [0]* num_nodes
time = 0

def main():
    ###  DFS on reverse graph
    explore = [0]* num_nodes
    for node in re_graph.keys():      # 大循环，遍历所有的点
        if explore[node-1]:
            continue
        else:
            rDFS(re_graph, node, explore)        # 小循环，每个点做 dfs


    ### DFS on orignial graph
    explore = [0]* num_nodes
    scc = list()

    for node in order:      
        if explore[node-1]:
            continue
        else:
            length = len(iDFS(graph, node, explore))     # 小循环，每个点做 dfs
            scc.append(length)
    
    scc = sorted(scc,reverse=True)
    print(scc[:52])



from collections import deque
def iDFS(graph, s, explore):    
    stack = deque()
    stack.append(s)
    chain = deque()
    
    while stack:
        tail = stack.pop()
        if explore[tail-1]:
            continue
        explore[tail-1] = 1
        chain.append(tail)

        for head in graph[tail]:       
            stack.append(head)
    return chain


def rDFS(graph, s, explore):
    global time
    
    explore[s-1] = 1
    
    for head in graph[s]:
        if explore[head-1]:
            continue
        else:
            rDFS(graph, head, explore)
    order[time-1] = s 
    time -= 1 


import sys
import threading
if __name__ == '__main__':      
    threading.stack_size(67108864) 
    sys.setrecursionlimit(2 ** 20)    
    thread = threading.Thread(target=main)        
    thread.start()