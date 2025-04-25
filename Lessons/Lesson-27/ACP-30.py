class circle():
    def __init__(self):
        self.radius=int(input("Enter the radius (cm):"))

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.radius * 3.141

c=circle()
print(f"Radius: {c.radius} cm")
print("Area of circle: {} cm²".format(c.area()))
print("Perimeter of circle: {} cm".format(c.perimeter()))

