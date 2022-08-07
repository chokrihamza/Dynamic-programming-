# the first implemention is not optimized

def fib(n):
    # base case
    if n<=1:return n
    return fib(n-1)+fib(n-2)
# time complexity is O(2^n) !!!!!!!
print(fib(0))
print(fib(1))
print(fib(5))
print(fib(6))
print(fib(100))  # takes many time to retun the result !!!!!!!

