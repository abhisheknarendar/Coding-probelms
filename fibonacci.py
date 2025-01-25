#fibonacci problem
n = int(input("Enter number of terms:"))
a = 0 
b = 1
end = " "
for i in range(n):
    print(a,end)
    temp = a+b
    a = b
    b = temp
