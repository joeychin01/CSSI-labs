num = raw_input("Please insert your number: ")
word = raw_input("Please insert your word: ")
if num == 1:
    word = word
else:
    if word[-3:] == "ife":
        word = word[:-3]+"ives"
    elif word[-2:] == "ch":
        word = word[:-2]+"ches"
    elif word[-2:] == "sh":
        word = word[:-2] + "shes"
    elif word[-2:] == "us":
        word = word[:-2]+"i"
    elif word[-2:] == "ay":
        word = word[:-2] + "ays"
    elif word[-2:] == "oy":
        word = word[:-2] + "oys"
    elif word[-2:] == "ey":
        word = word[:-2] + "eys"
    elif word[-2:] == "uy":
        word = word[:-2] + "uys"
    elif word[-1:] == "y":
        word = word[:-1] + "ies"
    else:
        word = word + "s"
print "%s %s" % (num, word)
