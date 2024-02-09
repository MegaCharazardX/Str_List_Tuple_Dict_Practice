# Program to increment The element of a list with a number.
print("This is a program to increment The element of a list with a number.")

Lst1 = []
Lst2 = []
num_elem = int(input("Enter the number of elements : "))
for i in range(num_elem):
    elem = int(input(f"Enter element number {i+1} : "))
    Lst1.append(elem)

num_incr = int(input("Enter the number increment elements : "))
for i in Lst1:
    Lst2.append(i + num_incr)

print(f"The original list : {Lst1}")
print(f"The incremented list : {Lst2}")