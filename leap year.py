#leap year
n = int(input("Enter a number:"))
if(n%4==0):
    if(n%100==0):
        if(n%400==0): #number must be divisible by 400 if divisible by 100
            print("Year is a leap year")
        else:
            print("Year is not a leap year")
            
    else:
        print("Year is a leap year")
    
    
else:
    print("Year is not a leap year")