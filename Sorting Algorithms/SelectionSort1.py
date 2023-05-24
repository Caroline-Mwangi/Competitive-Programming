class Solution: 
    def select(self, arr, i):
        for i in range(len(arr)):
            return arr[i]
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_val = i
            for j in range(i+1, n):
                if arr[min_val] > arr[j]:
                    min_val = j
                    
            arr[i], arr[min_val] = arr[min_val], arr[i]