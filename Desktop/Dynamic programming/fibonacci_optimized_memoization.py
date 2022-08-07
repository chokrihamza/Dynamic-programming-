# this  implemention is optimized by the use of memoization

def fib(n,memo={}):
    # add a condition for the memo elements
    if n in memo:return memo[n]
    # base case
    if n<=1:return n
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
# time complexity is O(2^n) !!!!!!!
print(fib(0))
print(fib(1))
print(fib(5))
print(fib(6))
print(fib(998))
print(fib(2000)) # wil generate an error about the size of the stack