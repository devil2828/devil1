def search(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1
arr=[2,50,90,6,1,30,800,75,22]
x=800
n=len(arr)
print ("the array with a given elements is : ")
print(arr)
result=search(arr,n,x)
if (result==-1):
    print("number is not present in arr")
else:
    print("element is present at index : ",result)
