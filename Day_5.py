# Assessment
# class Day_5:
#     def left_shift(self):
#         nums = list(map(int,input().split()))
#         l = len(nums)
#         k = int(input())
        # for i in range(k):
        #     # nums.append(nums.pop(0))
        #     first_ele = nums[0]
        #     for j in range(1,l):
        #         nums[j-1] = nums[j]
        #     nums[l-1] = first_ele
        # print(nums)
    #     k = k%l
    #     res = nums[k:]+nums[:k]
    #     print(res)
    # def right_shift(self):
    #     arr = list(map(int,input().split()))
    #     l = len(arr)
    #     k = int(input())
    #     k = k%l
    #     res= arr[k:]+arr[:k]
    #     print(res)
    # def occurance(self):
    #     arr = list(map(int,input().split()))
    #     max1 = 0
    #     ele = None
    #     for i in arr:
    #         j = arr.count(i)
    #         if j>max1:
    #             max1 = j
    #             ele = i
    #     print(ele)
# d1 = Day_5()
# d1.left_shift()
# d1.right_shift()
# d1.occurance()
#Strings: generic string, specific string
#There are three types of methods static,instance
# class Example:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Example.add(5,10))
# class method have access to class itself, allowing them to work with class level attributes which performs operations 
# that impacts entire class
# class SRU:
#     a = 10
#     @classmethod
#     def display(cls):
#         print(cls.a,"before modifying")
#     @classmethod
#     def modify(cls,num):
#         cls.a=num
#         print(cls.a,"after modifying")
# s = SRU()
# s.display()
# s.modify(777)
# Inheritance
# class Whatsapp1:
#     def text(self):
#         print("texting....!")
#     def audiocall(self):
#         print("calling...!")
# class Whatsapp2(Whatsapp1):
#     def videocall(self):
#         print("Connecting video..!")
#     def payments(self):
#         print("Transaction is successfull..!")
# class Whatsapp3(Whatsapp2):
#     def ai(self):
#         print("Command me...!")
# w3 = Whatsapp3()
# w3.audiocall()
# w3.payments()
# w3.ai()
# class Father:
#     def IQ(self):
#         print("Inherited Intelligence from Father!")
# class Mother:
#     def Appearance(self):
#         print("Inherited looks from Mother!")
# class Child(Father,Mother):
#     def OwnThoughts(self):
#         print("Following own idea!")
# ch1 = Child()
# ch1.IQ()
# ch1.Appearance()
# ch1.OwnThoughts()
# class Phone:
#     name = ''
#     def __init__(self,name):
#         self.name = name
#     def communication(self):
#         print(f"{self.name} is ringing")
#     def game(self):
#         print("Playing video games")
#     def media(self):
#         print("All audio,video and pics")
# class Phone1(Phone):
#     def __init__(self, name):
#         super().__init__(name)
#     def software(self):
#         print("Best android")
# class Phone2(Phone):
#     def __init__(self, name):
#         super().__init__(name)
#     def software(self):
#         print("iOS")
# i1 = Phone1("iphone")
# s1 = Phone2('Samsung')
# i1.communication()
# s1.communication()
# spiral matrix
n = int(input())
matrix = [[0]*n for _ in range(n)]
num=1
top,bottom,left,right = 0,n-1,0,n-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        matrix[top][i] = num
        num+=1
    top+=1
    for i in range(top,bottom+1):
        matrix[i][right] = num
        num+=1
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            matrix[bottom][i] = num
            num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            matrix[i][left] = num
            num+=1
        left+=1
for row in matrix:
    for i in row:
        print(i,end="\t")
    print()