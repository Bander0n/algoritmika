import random
A=int(input())
B=int(input())
lstA=[]
for i in range(A):
    lst2=[]
    for j in range(B):
        lst2.append(random.randint(1,100))
    lstA.append(lst2)

lstB=[]
for i in range(A):
    lst2=[]
    for j in range(B):
        lst2.append(random.randint(1,100))
    lstB.append(lst2)
print("Массив 1:")

for i in range(len(lstA)):
    for j in range(len(lstA[i])):
        print(lstA[i][j], end=' ')
    print()
    
print("Массив 2:")
for i in range(len(lstB)):
    for j in range(len(lstB[i])):
        print(lstB[i][j], end=' ')
    print()

    
result1=[]
result2=[]

for i in range(len(lstB)):
    lst2=[]
    for j in range(len(lstB[i])):
       lst2.append(lstA[i][j]+lstB[i][j])
    result1.append(lst2) 


print("Сумма:")
for i in range(len(result1)):
    for j in range(len(result1[i])):
        print(result1[i][j], end=' ')
    print()   

    
input()

