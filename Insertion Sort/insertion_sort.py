def insertionSort1(n, a):
    k=a[n-1]
    flag=False
    for i in range(n-1,0,-1):
        if i>0 and k<a[i-1]:
            a[i]=a[i-1]
            print(" ".join(a))
            if i==1:
                flag=True
        else:
            break
    if flag:
        arr[i-1]=k
    else:
        a[i]=k
        
    print(" ".join(a))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(str, input().rstrip().split()))

    insertionSort1(n, arr)
