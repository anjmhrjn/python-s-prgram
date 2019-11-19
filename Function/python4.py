#to print matrix based on user
def mtx(a,b):
    A=[]
    B=[]
    for i in range(a):

        for j in range(b):
            B.append(1)
        A.append(B)
        B=[]
        print(A[i])
    return A
a=int(input('Enter no. of rows:'))
b=int(input('Enter no. of columns:'))
(mtx(a,b))


# a=3
# b=4
# a1=[]
# for i in range(a):
#     a1.append([1]*b)
# print(a1)