import random
#List,Tuple,Set,Dict
#List is ordered, mutable and allows duplicates
# l = []
# l.append(12)
# l.insert(3,'Enigma')
# l.extend([3.14,'computer',962])
# l.pop()
# print(l)
# print(l[:-1])
#Tuple is order,immutable and allows duplicate values
# t = (3.14,25,"Haleluya",9398098)
# print(t)
#Set is unordered, immutable and doesn't allow duplicates
# s = set(map(int,input().split()))
# print(sorted(s))
#Dictionary: data stored in key value pair
# d = {
#     'Name':"Krishna",
#     'Age': 25
# }
# print(d.values())
#Range()
# n = int(input())
# # sum=0
# # for i in range(2,n+1,2):
# #     print(i)

# # for i in range(1,n+1):
# #     sum+=i;
# # print(sum)
# if (n>1=8):
#     print('Eligible')
# else:
#     print('Not eligible')
# print("Eligible" if int(input())>=18 else "not eligible")
# isrunning = False
# while ~isrunning:
#     gender = input("Enter gender:").lower()
#     if (gender == "female"):
#         address = input("Enter address:").lower()
#         if (address == "ts"):
#             print("Free ticket")
#             break
#         elif (address == 'ap'):
#             print("50% off")
#             break
#         else:
#             print("10% off")
#             break
#     elif (gender == "male"):
#         print("Not free")
#         break
#     else:
#         isrunning = True
#         print("Invalid! try again")

# income = int(input("Enter income:"))
# if income <=100000 and income >= 50000:
#     print("10% tax")
#     print("Remaining income:",(income - income*0.1))
# elif (income<50000 and income >=25000):
#     print("5% tax")
#     print("Remaining amount:",(income - income*0.05))
# else:
#     print("Tax free")
#     print("Your income:",income)
# m = int(input())
# n = int(input())
# for i in range(m,n+1):
#     count = 0
#     for j in range (1,i):
#         if (i%j == 0):
#             count+=1
#     if (count<2):
#         print(i)
# str = input()
# l = list(str)
# rev = l[::-1]
# print(rev)
# if (l == rev):
#     print("palindrome")
# else:
#     print("Not palindrome")
n = int(input())
s=0
p=1
while n!=0:
    x = n%10
    s+=x
    p*=x
    n//=10
if s==p:
    print("Spy num")
else:
    print("Not spy num")
