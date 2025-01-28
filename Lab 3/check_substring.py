def is_substring(str1, str2):
    return str1 in str2 or str2 in str1

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if is_substring(str1, str2):
    print("One string is present in the other.")
else:
    print("No string is present in the other.")
