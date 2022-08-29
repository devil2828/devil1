def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key


arr =[125,90,100,50,61,40,22]
print("befor sorting the array is :\n",arr)
insertion_sort(arr)
print("after sorting the array is : ")
for i in range(len(arr)):
    print("%d" % arr[i])
