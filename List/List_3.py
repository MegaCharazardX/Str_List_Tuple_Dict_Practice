# Program to input two list s and creates a third list, that contains all elements of the first followed by all elements
# of the second
print("This is a program to input two list s and creates a third list, that \
      contains all elements of the first followed by all elements of the second.")

Lst1 = []
Lst2 = []
Lst3 = []
num_elem = int(input("Enter the number of elements in list 1 : "))
for i in range(num_elem):
    elem = int(input(f"Enter element number {i+1} : "))
    Lst1.append(elem)

num_elem = int(input("Enter the number of elements in list 2 : "))
for i in range(num_elem):
    elem = int(input(f"Enter element number {i+1} : "))
    Lst2.append(elem)

Lst3.extend(Lst1)
Lst3.extend(Lst1 )

print(f"The first list : {Lst1}")
print(f"The second list : {Lst2}")
print(f"The third list : {Lst3}")
