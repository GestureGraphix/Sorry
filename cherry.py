import math
from turtle import *

def cherry_r(theta):
    return 30 * (3 - 3 * math.sin(theta))  # Scale factor increased to 30

def cherry_x(theta):
    return cherry_r(theta) * math.cos(theta)

def cherry_y(theta):
    return cherry_r(theta) * math.sin(theta)

speed(1000)
bgcolor("black")

# Write "Sorry"
up()
goto(-290, -70)  # Adjusted position for the apology
color("white")  # Changed color to white for the apology
write("Sorry", font=("Arial", 60, "bold"))  # Increased font size

# Shift the cherry and its stem to the right
shift_amount = 100  # Increased shift amount
up()
goto(shift_amount, 30)  # Adjusted x-coordinate for the center of the cherry
down()

# Draw the cherry
color("red")
begin_fill()
for i in range(361):
    theta = math.radians(i)
    goto(cherry_x(theta) + shift_amount, cherry_y(theta) + 30)  # Adjusted coordinates for the center of the cherry
end_fill()

# Draw the stem
up()
goto(shift_amount, 50)  # Adjusted position for the stem
down()
width(5)  # Adjusted width for the stem
color("green")  # Changed color to brown for the stem

# Draw half of the parabolic stem
stem_height = 120  # Increased stem height
for x in range(31):  # Increased the range for a longer stem
    y = -(x ** 2) / 30 + stem_height  # Equation of a downward parabola
    goto(x + shift_amount, y)

done()
