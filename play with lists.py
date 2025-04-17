Lst=[4,6,8,3,1,34,39,2]
print(Lst)

sum= 0
for i in Lst:
    sum +=i

avg= sum/len(Lst)

print("the sum of the numbers in the list is: ",sum)
print("\n the average of the numbers is: ",avg)

Lst.sort()

print("Smallest number: ",Lst[0])

print("\n Biggest number on list: ",Lst[-1])