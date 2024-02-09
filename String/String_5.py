# Program to prompt for a string.
# Extract all the characters from the string.
# If there are digits:
    # Sum the collected digits together.
    # Print out :
        # The original string.
        # The digits.
        # The sum of the digits
# If there are no digits :
    # Print the original string and message "String has no digits".
print("""Program to prompt for a string.
Extract all the characters from the string.
If there are digits:
    Sum the collected digits together.
    Print out :
        The original string.
        The digits.
        The sum of the digits
If there are no digits :
    Print the original string and message "String has no digits". """)


str_input = input("Enter a string : ")
sum_str_input = 0
digits = ""
for i in str_input :
    if i.isdigit() :
        sum_str_input += int(i)
        digits += i

if sum_str_input == 0 and len(digits) == 0 :
    print(f"{str_input} has no digits.")
else:
    print(f"The original string : {str_input}")
    print(f"The characters are : {digits}")
    print(f"The sum of all digits are  : {sum_str_input}")

