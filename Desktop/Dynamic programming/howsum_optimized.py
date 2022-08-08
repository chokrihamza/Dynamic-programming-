# this is a simple implementation 
# without optimization
def howSum(target,nums,memo={}):
    if target in memo :return memo[target]
    # base cases 
    if target==0:return []
    if target<0:return None 
    for num in nums:
        remainder=target-num
        remainderResult=howSum(remainder,nums)
        if remainderResult != None:
            memo[target]=[*remainderResult,num]
            return memo[target]
    memo[target]=None
    return memo[target]
    

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(100,[7,14])) # work very nice 
