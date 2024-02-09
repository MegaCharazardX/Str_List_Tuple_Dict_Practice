# Program to repeatedly prompt the user for a sentence or "q" to quit.
# Upon input of sentence, s, print the string produced from s by converting each lower case to capital & each capitalcase to lower.
# The other characters are left unchanged


while True : #s != 'q' or s != "Q":
    s = input("Enter a sentence(s) or Enter q to quit : ")
    if s.strip() == "q" or s.strip() == "Q":
        break
    else :
        print(s.swapcase())
        continue