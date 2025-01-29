#check palindrome
def palindrome(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
        
    if string == reversed_string:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
        
string1 = input("Enter string to check palindrome:")
palindrome(string1)
        