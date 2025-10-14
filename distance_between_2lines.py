x1, y1, x2, y2 = eval(input("Enter the coordinates of two lines, x1, y1, x2, y2 : "))
distance_between_two_lines = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

print("The distance betw line",(x1,y1,), "and", (x2,y2,), "is", distance_between_two_lines)