def gridTraveler(m,n):
    if m==1 and n==1:return 1
    if m==0 or n==0:return 0
    return gridTraveler(m-1,n)+gridTraveler(m,n-1)
    
    
    
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18)) # this will be so lazy because the program is not optimized 
