# Program to ask the user to enter a lis t of strings. 
# Create a new list that consists of those strings with their first characters removed.
print("This is a program to ask the user to enter a lis t of strings. Then \
    Create a new list that consists of those strings with their first characters removed.")

Lst1 = []
Lst2 = []
num_elem = int(input("Enter the number of elements : "))
for i in range(num_elem):
    elem = input(f"Enter string number {i+1} : ")
    Lst1.append(elem)

for i in range(len(Lst1)) :
    Lst2.append(Lst1[i][1:])

print(f"The original list : {Lst1}")    
print(f"The second list : {Lst2}")    