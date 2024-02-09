# Program to check if a number is present in a list or not. 
    # If present enter the position of it.
    # Else print an appropriate message.
print("This is a program to check if a number is present in a list or not.\
If present enter the position of it. Else print an appropriate message.")

Lst1 = []
while True :
    num_elem = input("Enter the number of elements : ")
    if num_elem.isdigit():
        num_elem = int(num_elem)
        break
    else :
        print("Invalid input")
        continue
for i in range(num_elem):
    elem = int(input(f"Enter element number {i+1} : "))
    Lst1.append(elem)

print(f"The original list : {Lst1}")    
num_find = int(input("Enter the number to search in the list : "))

if num_find not in Lst1 :
    print(f"The number {num_find} is not in the list {Lst1}.")

else:
    tmp_lst = Lst1
    for i in tmp_lst :
        if i == num_find :
            print(f"The number {num_find} is in the index .")
            tmp_lst.remove(i)
    