nums_1=[1,2,3]
nums_2=[4,5,6]
print(nums_1)
print(nums_2)
result=map(lambda x, y: x+y, nums_1, nums_2)
print("Addition of two lists:")
print(list(result))

nums=[1,2,3,4,5]
print(nums)
def sq(n):
    return n*n
square=list(map(sq,nums))
print("Square of numbers")
print(square)
