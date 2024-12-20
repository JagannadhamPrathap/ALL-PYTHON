# a = int(input("Enter n:"))
# if (a%400==0):
#     if (a%4==0):
#         print(a,"is Leap year")
#     else:
#         print(a,"is not Leap year")
# else:
#     print(a,"is not Leap year")
#print(a,"is Leap year" if a%4==0 else "is not Leap year")
# l = []
# for i in range(0,6):
#     k = int(input(f'Enter sub {i+1}:'))
#     l.append(k)
# print(f'Avg: {sum(l)/len(l)}')
# y = sum(l)/6
# if (y>=90 and y<=100):
#     print("O grade")
# elif(y>=80 and y<90):
#     print("A grade")
# elif(y>=70 and y<80):
#     print("B grade")
# elif (y>=60 and y<70):
#     print("C grade")
# elif(y>=50 and y<60):
#     print("D grade")
# else:
#     print("Fail")
n = int(input())
# fac = 1
# for i in range(1,n+1):
#     fac*=i
# print(fac)
count = 0
for i in range(1,n+1):
    if (n%i == 0):
        count+=1
if (count>2):
    print("Composite")
else:
    print("Prime")
#ASSESSMENT
# print(max(map(int,input().split())))
# print(sum(list(map(int,input()))))
# a,b = map(int,input().split())
# a,b=b,a
# print(a,b)
# print(eval(input()))