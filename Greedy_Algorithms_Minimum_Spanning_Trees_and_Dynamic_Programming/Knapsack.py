import numpy as np
import sys
sys.setrecursionlimit(3000)

def read_file1(name):
	data = list()
	with open('Knapsack1.txt', 'r') as f:
	    for line in f.readlines()[1:]:
	        line = line.strip()
	        for x in line.split(' '):
	            data.append(int(x))
	f.close()

	data = np.asarray(data)
	data = data.reshape(100,2)

	return data


def Knapsack1(data, capacity, items):
    weight = np.zeros((items+1,capacity+1) ,'i4')
    for i in range(1,items+1):
        for w in range(capacity+1):
            if w-data[i-1,1] < 0:
                weight[i,w] = weight[i-1,w]
            else:
                weight[i,w] = max(weight[i-1,w], weight[i-1,w-data[i-1,1]] + data[i-1,0] )
                
    return(weight)


def read_file2(name):
	data = list()
	with open(name, 'r') as f:
	    for line in f.readlines()[1:]:
	        line = line.strip()
	        for x in line.split(' '):
	            data.append(int(x))
	f.close()

	data = np.asarray(data)
	data = data.reshape(2000,2)
	sortdata = data[data[:,1].argsort()]

	return sortdata


capacity = 2000000
results = dict()
for w in range(0,capacity+1):
    results[(0,w)] = 0

def Knap(data, i, w):

    # print(i,w)
    if (i,w) in results.keys():
        return results[(i,w)]
    else:
        if w < data[i-1,1]:
            results[(i,w)] = Knap(data, i-1,w)
        else:
            results[(i,w)] = max(Knap(data, i-1, w), Knap(data, i-1, w-data[i-1,1]) + data[i-1,0] )
        return results[(i,w)] 


def main():
	data1 = read_file1('knapsack1.txt')
	A = Knapsack1(data1, 10000, 100)
	print(A[100,10000])
	data2 = read_file2('knapsack2.txt')
	a = Knap(data2, 2000, 2000000)
	print(a)


if __name__ == '__main__':
	main()