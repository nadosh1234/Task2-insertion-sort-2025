def insertion_sort(arr):
    n=len(arr)
    for j in range(1,n):
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i-=1
            arr[i+1]=key
mmm=[66,60,20,22,10,9]
insertion_sort(mmm)   
print ("new arr is:", mmm)     
