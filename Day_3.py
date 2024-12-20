# import random
# class DiesGame:
#     def throwDie(self):
#         return random.randint(1,6)
# p1 = DiesGame()
# print(p1.throwDie())
#In dictionay keys should be unique
# d = {
#     "Product":"Mobile",
#     "Brand":"Samsung",
#     "Price":55000,
#     "Processor speed":3.2
# }
# d.popitem()
# d.update({"color":"black"})
# print(d)
# print(d.clear())
# l = list(map(int,input().split()))
# i = 0
# for i in range(0,len(l)):
#     i+=1
#     if i not in l:
#         print(i)
# max1 = max(l)
# print((max1*(max1+1)/2)-sum(l))
#WAP to check whether given number is perfect number
# n = int(input())
# sum=0
# for i in range(1,n):
#     if n%i == 0:
#         sum+=i
# if sum == n:
#     print(n,"is perfect num")
# else:
#     print(n,"is not perfect num") 
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
#Strings: The literal which u write in single or double quotes are strings
# print("eeeeeffee".count("e"))
# s = input()
# count=0
# k = input()
# for i in s:
#     if i==k:
#         count+=1
# print(count)
# print("count".capitalize())
# str=input()
# print('palind' if str==str[::-1] else 'not palind')
# str1=input()
# str2 = ""
# for i in str1:
#     if i not in str2:
#         str2+=i
#     else:
#         print(i)
# print(str2)
# s1 = input()
# s2 = ""
# for i in s1:
#     if i.isupper():
#         s2+=i.lower()
#     elif i.islower():
#         s2+=i.upper()
# print(s2)
# print("PrAtHap".swapcase())
# class convert:
#     def SwapCase(self,s):
#         s2=""
#         if len(s)==0:
#             return s.upper()
#         else:
#             for i in s:
#                 if i.isupper():
#                     s2+=i.lower()
#                 elif i.islower():
#                     s2+=i.upper()
#             return s2
# c = convert()
# print(c.SwapCase(input()))
class Operation:
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a//b
    def OE(self,n):
        return "Odd" if n&1 else "even"
    def Prime(self,n):
        count=0
        for i in range(2,n//2):
            if n%i==0:
                count+=1
        if count>2:
            return "Composite"
        else:
            return "Prime"        
    def FizzBuzzz(self,n):
        if n%3==0 and n%5==0:
            return "FizzBuzz"
        elif n%5==0:
            return "Buzz"
        elif n%3==0:
            return "Fizz"
        else:
            return n

op1 = Operation()
# print(op1.OE(int(input())))
print(op1.Prime(int(input())))
# print(op1.FizzBuzzz(int(input())))