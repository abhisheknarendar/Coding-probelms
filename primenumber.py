#Prime number
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        #n**0.5 gives square root of n
        if(n%i==0):
            return False
            
    return True
    
n1 = int(input("Enter number to check for prime:"))
print(check_prime(n1))
