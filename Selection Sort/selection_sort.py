
class Solution: 
    def select(self, arr, i):
        small=i
        for j in range(i,len(arr)):
            if arr[small]>arr[j]:
                small=j
        return small
    
    def selectionSort(self, arr,n):
        for i in range(n):
            small=self.select(arr,i)
            arr[small],arr[i] = arr[i],arr[small]
        
        

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
#