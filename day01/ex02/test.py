from vector import Vector

# ----- SIZE ----- #
print(Vector(3).values)  # OK
# print(Vector(-5).values) # size < 0 OK

# ----- LIST ----- #
print(Vector([0.0, 1.0, 2.0, 3.0]).values)  # OK
# print(Vector([]).values)  # empty list
# print(Vector([0.0, 1, 2.0, 3.0]).values)  # aren't floats

# ----- TUPLE ----- #
print(Vector((10, 15)).values)  # OK
# print(Vector((10.0, 15)).values)  # aren't ints
# print(Vector((15,)).values)  # size of 2 tuple
# print(Vector((15, 10)).values)  # inverse range
# print(Vector((15, 15)).values)  # empty vector

# ----- BAD TYPE ----- #
# print(Vector(2.0).values)  # should be int
# print(Vector({}).values)  # should be int


V1 = Vector((5))
V2 = Vector((10, 5))
V3 = Vector([2.0, 3.0])
print(f"V1: {V1}")
print(f"V2: {V2}")
print(f"V3: {V3}")
# print('\n##### add #####')
# print(V1 + V1)
# print(V1 + 10)

# print('\n##### radd ######')
# print(V1 + V1)
# print(10 + V1)

# print('\n##### sub #####')
# print(V1 - V2)
# print(V1 - 10)

# print('\n##### rsub #####')
# print(V2 - V1)
# print(10 - V1)

print('\n##### mul #####')
print(V1 * V2)
print(V1 * 10)

print('\n##### rmul #####')
print(V2 * V1)
print(10 * V1)

print('\n##### div #####')
print(1 / V2)

print(V1.__repr__())
print(Vector.__init__.__doc__)
print(Vector.__doc__)
