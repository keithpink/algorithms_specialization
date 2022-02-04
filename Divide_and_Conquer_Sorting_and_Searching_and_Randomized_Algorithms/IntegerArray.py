def inver(ls):
   
    if len(ls) == 1:
        total_inver = 0
        sorted_ls = ls
    else: 
        left = ls[:len(ls)//2]
        right = ls[len(ls)//2:]
    
        (left_inver, sorted_left) = inver(left)
        (right_inver, sorted_right) = inver(right)
        (split_inver, sorted_ls) = merge_sort(sorted_left, sorted_right)
        
        total_inver = left_inver + right_inver + split_inver
    
    return total_inver, sorted_ls


def merge_sort(s1, s2):        

    i = 0
    j = 0
    split_inver = 0
    merged_ls = []
    
    while (i < len(s1)) and (j < len(s2)):
        if s1[i] <= s2[j]:
            merged_ls.append(s1[i])
            i += 1
        else:
            merged_ls.append(s2[j])
            j += 1
            split_inver += len(s1)-i
            
    while i < len(s1):
        merged_ls.append(s1[i])
        i += 1
        
    while j < len(s2):
        merged_ls.append(s2[j])
        j += 1
        
    return split_inver, merged_ls


def main():
    data = []
    with open("IntegerArray.txt","r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            data.append(int(line))
         
    total_inver, sorted_ls = inver(data)
    print(total_inver)

if __name__ == '__main__':
    main()

