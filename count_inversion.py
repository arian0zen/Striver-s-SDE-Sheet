'''For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
An inversion is defined for a pair of integers in the array/list when the following two conditions are met.
A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]' 
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').'''
#look at notebook, explanation written there (this one is personal note)
def mergeSort(arr, n):
    temp_arr = [0]*n
    return divide(arr, temp_arr, 0, n-1)
def divide(arr, temp_arr, left, right):
    count = 0
    if left  < right:
        mid = (left+right)//2
        count += divide(arr, temp_arr, left, mid)
        count += divide(arr, temp_arr, mid+1, right)
            
        count += conquer(arr, temp_arr, left, mid, right)
    return count
def conquer(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    count = 0
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            temp_arr[k] = arr[j]
            count += (mid-i)+1
            j += 1
            k +=1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
        
    for i in range(left, right+1):
        arr[i] = temp_arr[i]       
        
    return count

                


print(mergeSort([5,4,3,2,1,4, 0], 7))