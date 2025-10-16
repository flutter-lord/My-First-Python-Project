# r is the length from the center of the polygon to the vertex;
r = eval(input("Enter the length from the center of the polygon to the vertex : "))

# s = length of the sides
import math as m

s = 2 * r * (m.sin(m.pi / 5))

area = (3 * (m.sqrt(3)) * pow(s, 2)) / 2

print("The area of the pentagon is", format(area, ".2f"))