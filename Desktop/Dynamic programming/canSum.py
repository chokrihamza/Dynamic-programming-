# this implementation is not optimized 
def canSum(target,nums):
    # base case 
    if target==0: return True 
    if target<0:return False  # bounding condition
    for num in nums:
        remainder=target-num
        if canSum(remainder,nums):
            return True 
    
    return False
    

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(100,[7,14])) # the program hanging 
