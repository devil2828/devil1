def MergeSort(arr):
    if len(arr) > 1:
        a =len(arr)//2
        l = arr[ :a]
        r = arr[a: ]
        MergeSort(l)
        MergeSort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1    
            
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    arr =[55,2,0,25,100,60,9,7,8,80,3,30,45,1,22]
    print("Unsorted array is :\n", arr)
    MergeSort(arr)
    print("Sorted array is :")
    printList(arr)
