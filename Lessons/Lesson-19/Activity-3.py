L=[4,2,5,3,11,6,1,9]
print("Original List:",L)

count=0

for i in L:
    count+=1

avg=count/len(L)
print("Average=",avg)

L.sort()

print("The largest number in the list:",L[0])
print("The smallest number in the list:",L[-1])


