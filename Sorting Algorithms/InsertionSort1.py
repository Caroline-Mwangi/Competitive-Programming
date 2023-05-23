# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    sort_val = arr[-1]
    comp_val = n-2
    
    while (sort_val < arr[comp_val]) and (comp_val >= 0):
        arr[comp_val+1] = arr[comp_val]
        print(*arr)
        comp_val -= 1
    
    arr[comp_val+1] = sort_val
    print(*arr)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
