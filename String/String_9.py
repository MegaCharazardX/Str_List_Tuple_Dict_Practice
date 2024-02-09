# Program to take to strings from the user and diosplay the smallest number in the single line,
# And  the larger in the format

str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

if str1 > str2 :
    small = str2
    large = str1
elif str2 > str1 :
    small = str1
    large = str2
else :
    small = str1
    large = str2

print(small)

large_len = len(large)
for i in range (large_len//2):
    space1 = " "*i
    large_i = large[i]
    space2 = " " * (large_len-2*i)
    Large = large[large_len - i -1]

    print(space1, large_i, space2, Large , sep="")
