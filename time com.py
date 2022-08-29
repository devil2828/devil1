def findpair(a,n,z):
    for i in range(n):
        for j in range(n):
            if (i!=j and a[i]+a[j]==z):
                return True
    return False
a=[1,-2,1,0,5,10,6,8,5]
z=2
n=len(a)
print(a)
print("The pair of given array is : ")
if (findpair(a,n,z)):
    print("True")
else:
    print("False")
