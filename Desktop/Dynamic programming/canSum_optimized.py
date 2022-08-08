# this implementation is not optimized 
def canSum(target,nums,memo={}):
    if target in memo :return memo[target]
    # base case 
    if target==0: return True 
    if target<0:return False  # bounding condition
    for num in nums:
        remainder=target-num
        if canSum(remainder,nums,memo):
            memo[target]=True
            return True
    memo[target]=False
    return False
    

print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
