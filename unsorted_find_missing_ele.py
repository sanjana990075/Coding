arr=[1,2,3,4,6]
n=len(arr)
for i in range(1,n+1):
    if arr[i-1]!=i:
        print(i)
        break
        
