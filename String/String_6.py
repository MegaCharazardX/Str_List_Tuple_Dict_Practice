# Program to prompt for a sentence(s).
# It should then print the orignal sentence(s) and,
# The following statistics relating to the sentence.
    # Number of words
    # Number of characters (Including white-space & puntuation)
    # Percentage of characters that are alpha-numeric

sent = input("Enter a sentrnce(s) : ")
split_sent = sent.split(" ")
no_words = 0
no_char = len(list(sent))
no_digits = 0
for i in sent:
    if i.isdigit():
        no_digits += 1
        
for i in split_sent:
    if len(i.strip(" ")) > 0:
        no_words += 1

persent = (no_digits/no_char) * 100
print(f"Number of words : {no_words}")
print(f"Number of charecters : {no_char}")
print(f"Percentage of alpha-numeric characters : {persent}")