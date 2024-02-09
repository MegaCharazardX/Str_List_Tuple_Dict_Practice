
while True :
    num_input = int(input("Enter the number : "))
    if not isinstance(num_input, int):
            print("decimals can not be converted")
            continue
    if not (-1 < num_input < 5000):
        print("number out of range (must be 0-4999)")
        continue


    romanNumeralMap = (
                    ('M', 1000),
                    ('CM', 900),
                    ('D', 500),
                    ('CD', 400),
                    ('C', 100),
                    ('XC', 90),
                    ('L', 50),
                    ('XL', 40),
                    ('X', 10),
                    ('IX', 9),
                    ('V', 5),
                    ('IV', 4),
                    ('I', 1))


    if num_input == 0:
        print('N')

    result = ""
    for numeral, integer in romanNumeralMap:
        while num_input >= integer:
            result += numeral
            num_input -= integer
    print(result)

    op = input("Do you want to go again y/n :")
    if op == "Y" or op == "y" :
         continue
    else :
         break

# num = (100, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
# rom = ("M","CM","D","CD","C","XC", "L","XL","X","IX", "V","IV","I")
# result = ""
# for i in range(len(num)):
#     count = int(num_input / num[i])
#     result += str(rom[i] * count)
#     num_input -= num[i] * count
# print(result)