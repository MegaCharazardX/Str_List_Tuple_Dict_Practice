# Program to take to inputs : The first, integer & the second, string.
# From the string input exract all digits, in the order they occurred, from the string.
    # If no digits occur set extracted value as 0
# Add the integer input & the digits extracted from the string together as integers
# Print the output in the form : integer_input + string_digits = sum

print(""" Program to take to inputs : The first, integer & the second, string.
 From the string input exract all digits, in the order they occurred, from the string.
     If no digits occur set extracted value as 0
 Add the integer input & the digits extracted from the string together as integers
 Print the output in the form : integer_input + string_digits = sum\n""")


int_input = int(input("Enter an integer : "))
str_input = input("Enter a string : ")
str_digits = "0"
for i in str_input :
    if i.isdigit():
        str_digits += i
_sum = int_input + int(str_digits)
print(f"{int_input} + {str_digits} = {_sum}")