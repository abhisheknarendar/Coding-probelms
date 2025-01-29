#find if number is divisible by 27
def find_divisible_by_27(num):
    if(num%27 == 0):
        
        print("its a multiple of 27")

    else:
        print("it's not a multiple of 27")
        
num1 = int(input("Enter number to find if it's divisible by 27:"))
find_divisible_by_27(num1)