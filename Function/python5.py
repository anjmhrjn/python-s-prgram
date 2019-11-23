result=[['name','maths','eng','phy','com'],
        ['john',88.0,87.0,82.0,81.0],
        ['sam',72.0,77.0,73.0,90.0],
        ]

#to find average marks of each person
s1=0
a=len(result[1])
for i in range(1,len(result)):
    for j in range(1,len(result[1])):
        s1 +=result[i][j]
    print('Average of ',result[i][0],' is:',s1/(a-1))
    s1=0

#to find average marks in each subject
s2=0
b=len(result)
for i in range(1,len(result[1])):
    for j in range(1,len(result)):
        s2+=result[j][i]
    print('Average in ',result[0][i],' is:',s2/(b-1))
    s2=0