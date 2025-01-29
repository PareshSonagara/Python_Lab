
string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")
result = ""
i = 0
while i < len(string):
    if string[i:i+len(remove_string)] == remove_string:
        i += len(remove_string)
    else:
        result += string[i]
        i += 1
print("Final string:", result)
