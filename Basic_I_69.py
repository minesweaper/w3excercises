x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = x + y + z - a1 - a3

print("Ordered numbers: {} {} {}".format(a1, a2, a3))