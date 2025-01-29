x1 = int(input("Enter x-coordinate of point 1: "))
y1 = int(input("Enter y-coordinate of point 1: "))
x2 = int(input("Enter x-coordinate of point 2: "))
y2 = int(input("Enter y-coordinate of point 2: "))
x3 = int(input("Enter x-coordinate of point 3: "))
y3 = int(input("Enter y-coordinate of point 3: "))

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear")
else:
    print("The points are not collinear")
