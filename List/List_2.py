# Program to reverse a list of integers.
print("This is a program to reverse a list of integers.")

Lst1 = []
num_elem = int(input("Enter the number of elements : "))
for i in range(num_elem):
    elem = int(input(f"Enter element number {i+1} : "))
    Lst1.append(elem)

print(f"The original list : {Lst1}")    
Lst1.reverse()
print(f"The reversed list : {Lst1}")