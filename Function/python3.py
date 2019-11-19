#to check whether the letter is upper case or lower case
def ulcase(a):
    if a.isupper():
        b="upper case"
    else:
        b="lower case"
    return b
c=input('Enter a letter:')
print(ulcase(c))
