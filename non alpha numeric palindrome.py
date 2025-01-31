#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters andremoving all non-alphanumeric characters, it reads the same forward and backward.Alphanumeric characters include letters and numbers. a string s, return true if it is a palindrome, or false otherwise


string1 = input(("Enter string:"))

noalpha = ""

for char in string1:
    if char.isalnum():
        noalpha += char
noalphareverse = ""
for char in noalpha:
    noalphareverse = char+ noalphareverse
    
if(noalpha == noalphareverse):
    print("It's a palindrom")
    
else:
    print("It's not a palindrome")