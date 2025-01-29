#NTH Prime number
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        #n**0.5 gives square root of n
        if(n%i==0):
            return False
            
    return True
    

def nth_prime(pos):
    count = 0
    num = 1
    while count<pos:
        num+=1
        if(check_prime(num)):
            count +=1
            
    return num
    
pos1 = int(input("Enter nth prime number:"))
print(nth_prime(pos1))

        