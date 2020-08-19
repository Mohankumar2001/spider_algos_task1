def symmetry(a): 
      
    n = len(a)    
    flag = 0
      
    # Check if the string's length is odd or even 
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
          
    start1 = 0
    start2 = mid 
   #start comparing 1st and middle element and then increase the array index to next no.   
    while(start1 < mid and start2 < n): 
          
        if (a[start1]== a[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
       
    # Checking the flag variable to check if the string is symmetrical or not 
    if flag == 0: 
        return True
        
    else: 
        return False
        
n = int(input())
a = input()
value = True
t = n
i = -1
while(value and t>0):
    i = i+1
    value = symmetry(a[:t])
    t = int(t/2)
    print(t,value,i)
print(i)