def countFreq(arry,n):
    freq=dict()
    print("Frequency of an array :\n",arr,"is:")
    for i in arr:
        if i not in freq:
            freq[i]=0
        freq[i]+=1
    for x in freq:
        print(x,":",freq[x])
        print("the no is occured:",freq[x],"times!")
arr=[10,20,20,10,10,20,5,20]
n=len(arr)
countFreq(arr,n)
