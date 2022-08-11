def somme(arr1,arr2):
    carry=0
    res=[]
    i=0
    
    if len(arr1)< len(arr2):
        arr1,arr2=arr2,arr1
    arr2=arr2+[0]*(len(arr1)-len(arr2))
    while i<len(arr1) :
        if not arr2[i]:
            val=arr1[i]+carry
        val=arr1[i]+arr2[i]+carry
        carry=val//10
        val=val%10
        res.append(val)
        i+=1
    res.append(carry) if carry else res
    return res
        
        
       
    
    



print(somme([1,2,3],[5,8,9,2,2,2,2,2]))
