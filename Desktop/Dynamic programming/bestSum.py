# Not optimized solution brute force 
def bestSum(target,nums):
    if target==0 :return []
    if target<0:return None 
    
    bestfitSum=None 
    for num in nums:
        remainder=target-num
        remaiderReslut=bestSum(remainder,nums)
        if remaiderReslut is not None:
            remaiderReslut.append(num)
            if bestfitSum is None or len(remaiderReslut)<len(bestfitSum):
                bestfitSum=remaiderReslut.copy()
    
    return bestfitSum
    

print(bestSum(7,[2,3]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(7,[2,4]))
print(bestSum(8,[2,3,5]))
#print(howSum(100,[7,14])) # work very nice 
