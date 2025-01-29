def tolower(st):
    result = ""
    for char in st:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def toUpper(st):
    result = ""
    for char in st:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle(st):
    result = ""
    for char in st:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32) 
        else:
            result += char
    return result


word=input("Enter the string : ")
print(tolower(word))
print(toUpper(word))
print(toggle(word))
