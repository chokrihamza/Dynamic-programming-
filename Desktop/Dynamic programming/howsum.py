# this is a simple implementation 
# without optimization
def howSum(target,nums):
    # base cases 
    if target==0:return []
    if target<0:return None 
    for num in nums:
        remainder=target-num
        remainderResult=howSum(remainder,nums)
        if remainderResult != None:
            return [*remainderResult,num]
    
    return None
    

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
#print(canSum(100,[7,14])) # the program hanging 
