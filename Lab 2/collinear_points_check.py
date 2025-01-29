x1, y1 = input("Enter point 1 (x1 y1): ").split()
x2, y2 = input("Enter point 2 (x2 y2): ").split()
x3, y3 = input("Enter point 3 (x3 y3): ").split()

x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)
x3, y3 = int(x3), int(y3)

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear")
else:
    print("The points are not collinear")
