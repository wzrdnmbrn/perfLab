with open("circle.txt", "r") as f:
    center_x, center_y = map(float, f.readline().strip().split())
    radius = float(f.readline().strip())

with open("points.txt", "r") as f:
    for line in f:
        x, y = map(float, line.strip().split())
        distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
        radius_squared = radius**2

        if distance_squared < radius_squared:
            print(1)
        elif distance_squared > radius_squared:
            print(2)
        else:
            print(0)
