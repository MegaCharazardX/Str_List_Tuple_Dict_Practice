# a) List of integers 0 through 49
integers_list = []
for i in range(50):
    integers_list.append(i)

# b) List containing the squares of the integer 1 through 50
squares_list = []
for i in range(1, 51):
    squares_list.append(i**2)

# c) List ["a", "bb", "ccc", "dddd", ...] ending with 26 copies of the letter z
letter_list = []
for i in range(1, 27):
    letter_list.append(chr(ord('a') + i - 1) * i)

# Display the created lists
print("a) List of integers 0 through 49:")
print(integers_list)

print("\nb) List containing the squares of the integer 1 through 50:")
print(squares_list)

print("\nc) List ending with 26 copies of the letter z:")
print(letter_list)