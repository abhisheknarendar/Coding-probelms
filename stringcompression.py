#Write a program to compress a string by replacing consecutive repeating characters with their count, followed by the character. If a character occurs only once, append it as is.

def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count+=1
        else:
            if count>1:
                compressed_string+= str(count) + string[i-1]
            else:
                compressed_string += string[i-1]
            count = 1
    
    
    if count>1:
        compressed_string+= str(count)+string[-1]
    else:
        compressed_string+= string[-1]
    return compressed_string
string2 = input("Enter a string:")
print(compress_string(string2))
        
            