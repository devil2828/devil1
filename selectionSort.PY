def Selection_Sort(array):
    length=len(array)
    for i in range(length-1):
        minIndex = i
        for j in range(i+1, length):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array
array = [50,80,100,60,85,600,76,2,0,1,3]
print("Befor sorting the array was : \n", array)
print("After sorting the array is : \n",Selection_Sort(array))
   
