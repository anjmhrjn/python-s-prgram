def gre(a):
    b=a%2
    if b==0:
        c="even"
    else:
        c="odd"
    return c
x=int(input('Enter a no.'))
print(gre(x))
