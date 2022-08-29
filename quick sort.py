def partition(array,left,right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[j])
    (array[i + 1], array[right]) = (array[right], array[i + 1])
    return i + 1
def quickSort(array, left, right):
    if left < right:
        pi = partition(array, left,right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)
data = [50, 6, 0, 22, 30, 80, 100, 2, 4]
print("Unsorted Array :",data)
size = len(data)
quickSort(data, 0, size - 1)
print("\n Sorted array in Ascending order :",data)
