# Program to input a list containing numbers b/w 1 & 12
# Replace all the entry greater than 10 with 10
print("This is a program to input a list containing numbers b/w 1 & 12. Then \
    replace all the entry greater than 10 with 10.")

Lst1 = []
Lst2 = []
num_elem = int(input("Enter the number of elements : "))
i = 0
while i < num_elem :
    elem = int(input(f"Enter element number {i+1} : "))
    if elem >= 1 and elem <= 12 :
        i += 1
        Lst1.append(elem)
    else :
        print("Enter a number b/w 1 & 12.")

for j in Lst1 :
    if j > 10 :
        j = 10
        Lst2.append(j)
    else:
        Lst2.append(j)

print(f"The original list : {Lst1}")    
print(f"The second list : {Lst2}")  