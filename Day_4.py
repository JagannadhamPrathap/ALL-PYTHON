import math
#Patterns
#Escape sequence characters \n, \t
#OOPs is methadology which makes software development easier with the help of class, object
#There are four main principles which oops follows
#Inheritance, Polymorphism, Abstraction,Encapsulation
#We can create n number of obj for a class
class Day_4:
    # n = int(input())
    def pat1(self):
        print('\n'.join(i*"* " for i in range(self.n+1)))
    def escap(self):
        print('Hello it\'s my birthday today')
    def pat2(self):
        for i in range(self.n):
            print()
            for j in range(self.n-i-1,0,-1):
                print(" ",end="")
            for k in range(2*i+1):
                print("*",end="")
        print()
    def pat3(self):
        print("\n".join(self.n*"*" for i in range(self.n)))
    def pat4(self):
        print("\n".join(i*"*" for i in range(self.n,0,-1)))
    def enum(self):
        l = [3.14,7,"apple",123]
        l2=[]
        for i,v in enumerate(l):
            l2.append(i)
        print(l2)
    def rev_arr(self):
        arr = list(map(int,input().split()))
        first=0
        last=len(arr)-1
        while first<last:
            arr[first],arr[last] = arr[last],arr[first]
            first += 1
            last -= 1
        print(arr)
    def max_minarr(self):
        arr = list(map(int,input().split()))
        max1,min1=0,1
        for i in range(1,len(arr)):
            if max1<arr[i]:
                max1 = arr[i]
            if min1>arr[i]:
                min=arr[i]
        print(max1)
        print(min1)
    def check_sortarr(self):
        arr = list(map(int,input().split()))
        is_sorted=True
        for i in range(self.n-1):
            if arr[i] > arr[i+1]:
                is_sorted=False
        if is_sorted:
            print("sorted")
        else:
            print("UnSorted")
    def dupl_arr(self):
        arr = list(map(int,input().split()))
        res=[]
        for i in arr:
            if i not in res:
                res.append(i)
        print(res)
    def secMax_arr(self):
        arr = list(map(int,input().split()))
        max1 = 1
        max2=arr[0]
        for i in arr:
            if i>max1:
                max1 = i
        print(max1)
        for i in arr:
            if i>max1:
                max2 = i
        print(max2)
    def pat5(self):
        for i in range(self.n):
            for j in range(i):
                print(" ",end='')
            for k in range(2*(self.n-i)-1):
                print("*",end="")
            print()
    def hcf(self):
        a,b = int(input()),int(input())
        m = min(a,b)
        for i in range(1,m+1):
            if a%i==0 and b%i==0:
                k = i
            print(k)
    def lcm(self):
        a = int(input())
        b = int(input())
        m = max(a,b)
        while True:
            if m%a==0 and m%b==0:
                print(m)
                break
            m+=1
    def Arm(self):
        x = int(input())
        sum = 0
        k = x
        l = len(str(x))
        while x!=0:
            j = x%10
            sum = sum+(j**l)
            x//=10
        if sum == k:
            print("Armstrong")
        else:
            print("Not Armstrong")
# Day_4().pat1()
# Day_4().escap()
# Day_4().pat2()
# print("Square:")
# Day_4().pat3()/
# Day_4().pat4()
# Day_4().enum()
#Day_4().rev_arr()
# Day_4().max_minarr()
# Day_4().check_sortarr()
# Day_4().dupl_arr()
# Day_4().secMax_arr()
# Day_4().pat5()
# Day_4().hcf()
# Day_4().lcm()
Day_4().Arm()
