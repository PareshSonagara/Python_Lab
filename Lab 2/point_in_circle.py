x_center, y_center = input("Enter center of circle (x y): ").split()
x_center, y_center = int(x_center), int(y_center)
radius = int(input("Enter radius of the circle: "))
x, y = input("Enter point (x y): ").split()
x, y = int(x), int(y)

dx = x - x_center
dy = y - y_center
distance_squared = dx * dx + dy * dy
radius_squared = radius * radius

if distance_squared < radius_squared:
    print("The point is inside the circle")
elif distance_squared == radius_squared:
    print("The point is on the circle")
else:
    print("The point is outside the circle")
