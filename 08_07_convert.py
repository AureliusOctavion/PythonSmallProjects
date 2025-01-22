# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1) Convert an int to a float

int_var = 32
int_var = float(int_var)
type(int_var)
print(int_var)


# 2) Convert a float to an int

float_var = 2.5
float_var = int(float_var)
type(float_var)
print(float_var)

# 3) Perform division using a float and an int

int_var = 22
float_var = 34.5
division = float_var / int_var
print(division)

# 4) Use two variables to perform a multiplication.

variable_one = 34
variable_two = 46

multiplication = variable_one * variable_two

print(multiplication)

# The information lost would be seen through the converting a float to an int conversion.