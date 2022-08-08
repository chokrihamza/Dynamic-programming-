def gridTraveler(m,n,memo={}):
    # add a condition for the memo 
    # lets create our key for the memo dict 
    key=str(m)+'.'+str(n)
    if key in memo:return memo[key]
    if m==1 and n==1:return 1
    if m==0 or n==0:return 0
    memo[key]=gridTraveler(m-1,n,memo)+gridTraveler(m,n-1,memo)
    return memo[key]
    
    
    
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
