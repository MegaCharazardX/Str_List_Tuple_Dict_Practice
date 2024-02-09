# Program to count the number of times a character occurs in a given string.
print("This is a program to count the number of times a character occurs in a given string.")

str_input = input("Enter a string : ")
sub_str = input("Enter the count the character : ")
count = str_input.count(sub_str)
if count == 0 :
    print(f"The string : '{str_input}' does not contain : '{sub_str}'.")
else :
    print(f"The string : '{str_input}' contains '{sub_str}', '{count}' times .")