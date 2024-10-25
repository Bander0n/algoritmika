import random
n=int(input())
lst=[]
for i in range(n):
    lst.append(random.randint(0,100))
print(lst)
max1=0
for i in range(n):
    summ=0
    for j in range(i,n):
        summ=summ+lst[j]
        if summ % 5 == 0 and summ>max1:
            max1=summ
print(max1)
            
