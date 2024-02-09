# Program to replace all vowels in the string with '*'.
print("This is a program to replace all vowels in the string with '*'.")

str_input = input("Enter a string : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
str_output = ""
for i in str_input:
    if i in vowels :
        i = "*"
        str_output = str_output + i
    else:
        str_output = str_output + i
print(f"The output : {str_output}")