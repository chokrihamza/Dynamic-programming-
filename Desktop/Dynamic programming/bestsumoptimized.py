def bestSum(target,nums,memo={}):
    if target in memo :return memo[target]
    if target==0 :return []
    if target<0:return None 
    
    bestfitSum=None 
    for num in nums:
        remainder=target-num
        remaiderReslut=bestSum(remainder,nums,memo)
        if remaiderReslut is not None:
            remaiderReslut.append(num)
            if bestfitSum is None or len(remaiderReslut)<len(bestfitSum):
                bestfitSum=remaiderReslut.copy()
    memo[target]=bestfitSum
    return bestfitSum
    

print(bestSum(7,[2,3]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(7,[2,4]))
print(bestSum(8,[2,3,5]))
print(bestSum(100,[1,2,5,25])) # work very nice 
