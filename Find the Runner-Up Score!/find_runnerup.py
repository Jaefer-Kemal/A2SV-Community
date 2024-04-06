if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if max!=arr[i]:
            print(arr[i])
            break
# it took 4 minutes