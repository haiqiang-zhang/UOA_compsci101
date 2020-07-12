def get_left_most_x(points):
    smallest_x = points[0][0]
    for index in range(len(points)):
        if points[index][0] < smallest_x:
            smallest_x = points[index][0]
    return smallest_x



points = [(100,5), (20, 100), (140, 200), (70, 100), (25, 0)]
print("Smallest x value:", get_left_most_x(points))
points = [(100,5), (20, 100), (140, 200), (70, 100), (25, 0), (1, 450), (450, 0)]
print("Smallest x value:", get_left_most_x(points))