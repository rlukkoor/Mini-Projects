def lengthOfLastWord(s):
    length = 0
    a = s.strip()
    
    for i in range(len(a)):
        if a[i] == " ":
            length = 0
        else:
            length += 1
    return length

print(lengthOfLastWord("Hello World"))