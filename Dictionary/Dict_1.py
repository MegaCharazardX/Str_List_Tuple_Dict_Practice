

key = []
num_elem = int(input("Enter the number of keys : "))
i = 0
while i < num_elem:
    elem = str(input(f"Enter key number {i+1} : "))
    if elem.isalpha():
        key.append(elem)
        i += 1
        continue
    else :
        print("!!The Key Must Be A String!!")
        continue

print(f"The keys : {key}")

val = []
i = 0
while i < num_elem:
    elem = input(f"Enter value number {i+1} : ")
    if elem.isalpha():
        print("!!The Key Must Be A Integer!!")
        continue
    elif elem.isdigit():
        val.append(int(elem))
        i += 1
        continue
    else :
        val.append(int(elem))
        i += 1
        continue

print(f"The Values : {val}")

employee = dict(zip(key, val))

print(f"The Dictionary : {employee}")

print("#*"*28, "ALTER", "#*"*28)

num_elem = int(input("Enter the number of employe : "))
EmployeDict = {}
for i in range(num_elem):
    print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
    key = input(f"Enter key number {i+1} : ")
    value = int(input(f"Enter value number {i+1} : "))
    EmployeDict[key] = value

print(f"The Dictionary : {EmployeDict}")