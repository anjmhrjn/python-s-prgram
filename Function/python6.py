#to print the sum of odd nos. from the range provided by user
def sodd(a):
    s1=0
    for i in range(a+1):
        if i%2!=0:
            s1+=i
            print(s1)
    return s1
a=int(input('Enter your range:'))
print('Total sum is:', sodd(a))