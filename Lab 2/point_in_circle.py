x_center = int(input("Enter x-coordinate of the circle center: "))
y_center = int(input("Enter y-coordinate of the circle center: "))
radius = int(input("Enter radius of the circle: "))
x = int(input("Enter x-coordinate of the point: "))
y = int(input("Enter y-coordinate of the point: "))

# Calculate squared distance without math.sqrt
distance_squared = (x - x_center) * (x - x_center) + (y - y_center) * (y - y_center)
radius_squared = radius * radius

# Compare the squared values to avoid using square root
if distance_squared < radius_squared:
    print("The point is inside the circle")
elif distance_squared == radius_squared:
    print("The point is on the circle")
else:
    print("The point is outside the circle")
