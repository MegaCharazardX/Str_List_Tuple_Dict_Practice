# Program to prompt for a phone number of 10 digits & two dashes, with dashes after the area code & the next three number.
print("This is a program to prompt for a phone number of 10 digits & two dashes, with dashes after the area code & the next three number.")

ph_no = input("Enter the phone number : ")

if len(ph_no) == 12 :
    if ph_no[3] == "-" and ph_no[7] == "-":
        if (ph_no[:3] + ph_no[4:7] + ph_no[8:]).isdigit() :
            print(f"The number {ph_no} is valid")
else :
    print(f"The number {ph_no} is not valid")
