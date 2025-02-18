list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))
for i in range(n1):
    num = int(input("Enter element: "))
    list1.append(num)

n2 = int(input("Enter number of elements in second list: "))
for i in range(n2):
    num = int(input("Enter element: "))
    list2.append(num)

difference_list = [x for x in list1 if x not in list2]
print("Elements in first list but not in second:", difference_list)
