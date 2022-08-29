def chkpair(a,size,x):
    for i in range(+0,size-1):
        for j in range(i+1,size):
            if (a[i]+a[j]==x):
                print(f"pair with the given sum{x}is({a[i],a[j]})")
                return 1
    return 0
if __name__=="__main__":
    a=[0,-1,2,-3,1,55]
    x=-2
    size=len(a)
if(chkpair(a,size,x)):
    print("valid pair exists for the value",x)
else:
    print("no valid pair exists for the value",x)
