# get an input from user and capitalize all of them, similarly iterate them and print individually
# a=input('Enter a sentence: ')
# b=a.upper()
# print(b)
#
# for i in a:
#     print(i)

#'today is monday' --> 'todayismonday'
a='today is monday'
b=a.split(' ')
c=''.join(b)
print(c)

d=a.replace('today','yesterday') #replace today with yesterday
print(d)

e='#'.join(b)    # today#is#monday
print(e)

print(e.replace('#',' '))   #back to 'today is monday'