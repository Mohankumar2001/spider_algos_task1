def nextno(num1,l): 
   
    num = list(num1); 
  
    # examine bits from the right 
    i = l-1; 
    while(i >= 0): 
        # if '0' is encountered, convert it to '1' and then break 
        if (num[i] == '0'): 
            num[i] = '1'; 
            break; 
  
        # else convert '1' to '0' 
        else: 
            num[i] = '0'; 
        i-=1; 
  
    num1 = ''.join(num); 
    if (i < 0): 
        num1 = '1' + num1; 
  
    return num1;


def prevno(num1,n): 

    num = list(num1); 
  
    # if the number is '1' 
    if (num1 == "1"): 
        return "0"; 
    i = n - 1; 
      
    # examine bits from right to left 
    while (i >= 0): 
  
        # if '1' is encountered, convert it to '0' and then break 
        if (num[i] == '1'): 
            num[i] = '0'; 
            break; 
  
        # else convert '0' to '1' 
        else: 
            num[i] = '1'; 
        i -= 1; 
  
    # if only the 1st bit in the binary representation was '1' 
    if (i == 0): 
        return num[1:n]; 
  
    # final binary representation of the required number 
    return '' . join(num); 


n = int(input())
num = input()
#for the two strings find previous and next binary no. of the given one
prev = prevno(num,n)
nxtno = nextno(num,n)
if len(prev)!=n or len(nxtno)!=n:
    print("-1")
else:
    print(prev,nxtno)
























