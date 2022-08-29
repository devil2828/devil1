def bubbleSort(A):
    for i in range(n):
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                a=A[j]
                A[j]=A[j+1]
                A[j+1]=a
A=[-4,5,-3,8,4]
print("Given array is UNSORTED ARRAY IS : ",A)
n=len(A)
bubbleSort(A)
print("Sorted array in ascending order is : ")
print(A)
