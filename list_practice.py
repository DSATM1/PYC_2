#print("Hello World!")

"""n = int(input("Enter size: "))
nums = []
for i in range(n):
    value = input("Enter Names: ")
    nums.append(value)
print(nums)
for i, name in enumerate(nums):
     print(f"{i+1}. {name}")"""

"""odds = [i for i in range(1, 21) if i % 2 == 1]
print(odds)"""

"""def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
lst = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(lst)
print(result)"""

"""age,name,city = input("Enter your age, name, city:").strip().split()
age =int(age)
name = name
city = city

print("Your age:", age)
print("Your city:", city)
print("Your name:", name)"""

"""day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")"""
        
"""x = 10
y = 5

match x + y:
    case 15:
        print("Result is 15.")
    case 20:
        print("Result is 20.")
    case _:
        print("No match found.")"""

"""grade = 'A'

match grade:
    case '0':
        print("Excellent!")
    case 'B':
        print("Good!")
    case _:
        print("Not specified.")"""


"""x = -23
print("x is positive" if x > 0 else "x is negative")"""

"""x = -0
print("x is positive" if x > 0 else ("x is negative" if  x < 0  else "x is zero" )) """

"""n = [19,23,34,42,51]
for num in n:  #foreach loop
    print(num)"""


"""i,j=1,10
while i <= 5 and j > 0:
    print("i = ", i , " j = ",j)
    i += 1
    j -= 1"""

"""for i in range(1,4):             #1 2 3
    for j in range(1,4):            #2 4 6
        print(i*j,end= " ")         #3 6 9
    print()"""



"""class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def start(self):
        print("Car Started")"""




"""class Dog:
    def __init__ (self):
        self.Bark = ""
        self.Run = ""

    def running(self):
        print(f"{self.Run} is Running")

    def stoped(self):
        print(f"{self.Run} is Stopped")

if __name__ == "__main__":
    myDog = Dog()
    myDog.Bark = "Pug " 
    myDog.Run ="Pug"

    print("My Dog Name is : ",myDog.Bark)
    myDog.running()
    myDog.stoped()"""




"""class Stack:
    def __init__(self):
        self.arr = [0]*5
        self.top = -1

    def push(self,x):
        if self.top == 4:
            print("Stack Overflow")
            return 
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return 
        popped_val = self.arr[self.top]
        self.top -= 1
        return popped_val

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.arr[i], end =" ")
        print()

if __name__ == "__main__":
    s =Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)

    print("Stack elements: ", end = "")
    s.display()

    s.pop()
    s.pop()

    print("After pop: ", end = "")
    s.display()"""



"""con = True
i = 0
while con:
    if i == 10:
        break
    print("Con is True",i)
    i += 1
print("Ok")"""
