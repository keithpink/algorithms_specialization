def partition1(A,l,r):
    # first element as pivot
    p = A[l]
    i = l+1   
    
    for j in range(l+1,r+1):
        if A[j] < p:
            A[i], A[j] = [A[j], A[i]]    # swap
            i += 1
        
    A[l], A[i-1] = [A[i-1], A[l]]
    return A, i-1



def partition2(A,l,r):
    # last element as pivot
    A[l], A[r] = [A[r], A[l]]
    p = A[l]
    i = l+1   
    
    for j in range(l+1,r+1):
        if A[j] < p:
            A[i], A[j] = [A[j], A[i]]    # swap
            i += 1
        
    A[l], A[i-1] = [A[i-1], A[l]]
    return A, i-1



def partition3(A,l,r):
    # three of the median
    if len(A)%2 ==0:
        k = len(A)//2-1
    else:
        k = len(A)//2
    
    pivot = sorted( [A[l],A[k],A[r]] )[1]
    
    if A[k] == pivot:
        A[l], A[k] = [A[k], A[l]]
    elif A[r] == pivot:
        A[l], A[r] = [A[r], A[l]]
        
    p = A[l]
    i = l+1   
    
    for j in range(l+1,r+1):
        if A[j] < p:
            A[i], A[j] = [A[j], A[i]]    # swap
            i += 1
        
    A[l], A[i-1] = [A[i-1], A[l]]
    return A, i-1



def QuickSort(ls, partition):
    comparison = 0
    n = len(ls)
    
    if n < 2:
        sorted_list = ls
    else:    
        A, p = partition(ls,0,n-1)
        comparison += (n-1)
    
        left_list, left_count = QuickSort(A[:p], partition)
        right_list, right_count = QuickSort(A[p+1:], partition)
        sorted_list = left_list + [A[p]] + right_list
        comparison += left_count + right_count

    return sorted_list, comparison



def main():
    data = []
    with open("QuickSort.txt","r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            data.append(int(line))

    for p in (partition1,partition2,partition3):
        sorted_list, comparison = QuickSort(data, p)
        print(comparison)



if __name__ == '__main__':
    main()


