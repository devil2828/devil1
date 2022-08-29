def count_Freq(arr,n):
    visited = [False for i in range(n)]
    for i in range(n):
        if(visited[i] == True):
            continue
        count = 1
        for j in range(i + 1,n,1):
            if(arr[i]== arr[j]):
                visited[j]=True
                count += 1
        print(arr[i],":", count)
        print("the no is occured",count,"times!")
if __name__ == '__main__':
    arr=[10,50,22,10,50,10,10,22]
    print(arr)
    n=len(arr)
    count_Freq(arr,n)
