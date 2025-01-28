def to_lower(string):
    result = ""
    for char in string:
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper(string):
    result = ""
    for char in string:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(string):
    result = ""
    for char in string:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        elif "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

string = input("Enter a string: ")

print("Lower case:", to_lower(string))
print("Upper case:", to_upper(string))
print("Toggle case:", toggle_case(string))
