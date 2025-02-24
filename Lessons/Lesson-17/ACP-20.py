import math

angle=float(input("Enter the angle in degrees:"))
radians= math.radians(angle)

sin=math.sin(radians)
cos=math.cos(radians)
tan=math.tan(radians)

print("Sin({angle})=",sin )
print("Cos({angle})=",cos )
print("Tan({angle})=",tan )
