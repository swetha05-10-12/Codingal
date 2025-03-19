print("Area Calculator")
len=int(input("Enter the length of the rectangle:"))
width=int(input("Enter the width of the rectangle:"))

def calculate_area(len,width):
    area=len*width
    return area

print("The area of your rectangle is:",calculate_area(len,width))

