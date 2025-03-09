import array as arr

array_num= arr.array('i',[1,3,5,3,7,9,3])
print("Original array:"+str(array_num))
print("The number of occurenecs of the number 3 in said array:"+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of items:")
print(str(array_num))
