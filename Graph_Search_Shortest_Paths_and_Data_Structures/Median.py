import heapq
data = list()
with open("Median.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line: 
            data.append(int(line))


def MM(data):       # median maintenance
    Min = list()     # 最小堆 储存比中位数大的数
    Max = list()    # 最大堆 储存比中位数小的数
    heapq.heapify(Min)
    heapq.heapify(Max)
    
    median = []     # 初始值 0
    med = data[0]
    
    for (i,num) in enumerate(data):             
        if i%2 == 0:         # 奇数情况
            if num <= med:
                heapq.heappush(Max, -num)
            else:
                m = heapq.heappushpop(Min, num)
                heapq.heappush(Max, -m)
                med = -Max[0]
        else:                 # 偶数情况
            if num >= med:
                heapq.heappush(Min, num)
            else:
                heapq.heappush(Min, med)
                heapq.heapreplace(Max, -num)
                med = -Max[0]

        median.append(med)
        i += 1
        # print(Max, Min)
    return median

print(sum (MM(data)))