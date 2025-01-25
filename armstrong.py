#Armstrong number
n = int(input("Enter number:"))

number_of_digits = 0
temp = n
while temp>0:
    temp = temp//10
    number_of_digits+= 1

powered_answer = 0
temp = n
while temp>0:
    digit = temp%10
    powered_answer += digit**number_of_digits
    temp//= 10
    
if n == powered_answer:
    print("It is an armstrong number ")
    
else:
    print("It is not an armstong number ")
