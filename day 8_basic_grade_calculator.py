name=input("enter your name")
n=int(input("enter number of subjects"))
marks = []
for i in range (0,n):
    m=int(input("enter marks"))
    marks.append(m)
average= sum(marks)/n
if average>=90:
    print(name ," , you got ",average,"and grade A")
elif average>=80:
    print(name ," , you got ",average,"and grade B")
elif average>=70:
    print(name ," , you got ",average,"and grade C")
elif average>=60:
    print(name ," , you got ",average,"and grade D")
else:
    print(name ," , you got ",average,"and you failed .")

