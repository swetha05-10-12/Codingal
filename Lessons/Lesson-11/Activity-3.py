row_size = int(input("Enter the number of rows for your diamond: "))
if row_size % 2 == 0:
    halfDiam_row = row_size // 2
else:
    halfDiam_row = (row_size // 2) + 1
space = halfDiam_row - 1
for i in range(1, halfDiam_row + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space -= 1
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()
space = 1
for i in range(1, halfDiam_row):
    for j in range(1, space + 1):
        print(end=" ")
    space += 1
    num = 1
    for j in range(1, 2 * (halfDiam_row - i)):
        print(num, end="")
        num += 1
    print()

    