def read_file(name):
    data = list()
    with open(name,'r') as f:
        for line in f.readlines():
            line = int(line.strip('\n'))
            data.append(line)
    f.close()
    
    return sorted(data)


def TwoSum(data, trange):
    sumset = list()
    i = 0
    j = len(data)-1
    
    while i < j:
        s = data[i] + data[j]
        if s < trange[0]:
            i += 1
        elif s > trange[1]:
            j -= 1
        else:
            k = j
            while data[i]+data[k] >= trange[0]:
                if data[i] != data[k]:
                    sumset.append(data[i]+data[k])
                    # print(sumset)
                k -= 1
            i += 1
            
    return set(sumset)


def main():
    data = read_file('prob-2sum.txt')
    trange = [-10000,10000]
    print(len(TwoSum(data, trange)))


if __name__ == "__main__":
    main()