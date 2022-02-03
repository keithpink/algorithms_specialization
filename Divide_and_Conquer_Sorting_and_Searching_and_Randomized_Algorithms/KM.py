def KM(n1, n2):
    len1 = len(n1)
    len2 = len(n2)
    
    if len1==1 and len2==1:
        prod = int(n1)*int(n2)
    elif len1 < len2:
        prod = KM(n1,n2[0:len2-len1])*(10**(len1)) + KM(n1,n2[-len1:])
    elif len1 > len2:
        prod = KM(n1[0:len1-len2],n2)*(10**(len2)) + KM(n1[-len2:],n2)
    else:
        a = n1[0:len1//2]
        b = n1[len1//2:]
        c = n2[0:len2//2]
        d = n2[len2//2:]

        m1 = KM(a,c)
        m2 = KM(b,d)
        ab = str(int(a) + int(b))
        cd = str(int(c) + int(d))
        m3 = KM(ab,cd)-m1-m2
        prod = m1*(10**(2*len1-2*(len1//2))) + m3*(10**(len1-len1//2)) + m2
    return prod

    n1 = 3141592653589793238462643383279502884197169399375105820974944592
    n2 = 2718281828459045235360287471352662497757247093699959574966967627
    KM(n1,n2)