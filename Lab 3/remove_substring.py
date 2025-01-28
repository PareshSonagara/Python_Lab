def remove_substring(main_str, sub_str):
    result = ""
    i = 0
    while i < len(main_str):
        if main_str[i:i + len(sub_str)] == sub_str:
            i += len(sub_str)
        else:
            result += main_str[i]
            i += 1
    return result

main_str = input("Enter the main string: ")
sub_str = input("Enter the string to remove: ")

final_str = remove_substring(main_str, sub_str)
print("Final string:", final_str)
