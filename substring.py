# substring of string

s1 = "sak"
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        print(s1[i:j])