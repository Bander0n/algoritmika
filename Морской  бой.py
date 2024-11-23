mas1 = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
lst=["A","B","C","D","E","F","G","H"]
print("Игрок 1")
p1=0
p2=0
for i in range(4):
    location=str(input("введите расположение -го корабля: "))
    p1=int(location[1])-1
    p2=lst.index(location[0])
    mas1[p1][p2]=1
    
print("  A B C D E F G H")
for i in range(len(mas1)):
    print(i+1, end=' ')
    for j in range(len(mas1[i])):
        print(mas1[i][j], end=' ')
    print()

    
mas2 = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print("Игрок 2")
d1=0
d2=0
for i in range(4):
    location=str(input("введите расположение -го корабля: "))
    d1=int(location[1])-1
    d2=lst.index(location[0])
    mas2[d1][d2]=1

print("  A B C D E F G H")
for i in range(len(mas2)):
    print(i+1, end=' ')
    for j in range(len(mas2[i])):
        print(mas2[i][j], end=' ')
    print()


shot1=4
shot2=4
while shot1>0 and shot2>0:
    bom1=input("Игрок 1,стреляйте!")
    i=int(bom1[1])-1
    j=lst.index(bom1[0])
    if mas2[i][j]==1:
        mas2[i][j]=0
        shot2=shot2-1
        print("Есть поподание!")
    else:
        print("Промазал")
    if shot2<=0:
        break
    bom2=input("Игрок 2,стреляйте!")
    i=int(bom2[1])-1
    j=lst.index(bom2[0])
    if mas1[i][j]==1:
        mas1[i][j]=0
        shot1=shot1-1
        print("Есть поподание!")
    else:
        print("Промазал")
if shot1>shot2:
    print("Игрок 1 выйграл")
else:
    print("Игрок 2 выйграл")
input()
