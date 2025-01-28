#show negative numbers as positive when addition or subtraction is performed on 2 numbers

def add(a,b):
    c = a+b
    if(c<0):
        return -c
    else:
        return c
  
    
def sub(a,b):
    c = a-b
    if(c<0):
        return -c
    else:
        return c
n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))
print(f"Addition of two values {n1} and {n2} is {add(n1,n2)}")
print(f"Addition of two values {n1} and {n2} is {sub(n1,n2)}")

    