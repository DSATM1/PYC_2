#print("List Practice Set")

"""reverse_list([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
   reverse_list(["a", "b", "c"]) → ["c", "b", "a"]"""

"""def reverse_list(lst): #type:ignore
   res = []
   i = len(lst) - 1  #type:ignore
   while i>= 0:
      res.append(lst[i])  #type:ignore
      i = i - 1
   return res #type:ignore
print(reverse_list([1, 2, 3, 4, 5])) #type:ignore
print(reverse_list(["a","b","c","d","e"])) #type:ignore"""


"""lst = [1, 2, 3, 4, 5]

reverse_list = []

i = len(lst) - 1

while i >= 0:
    reverse_list.append(lst[i])
    i = i - 1

print(reverse_list)"""

"""def palindrome(pal):
    return pal == pal[::-1]
res = palindrome("madaM")
print(res)"""



"""is_fail = True
i = 0
while is_fail:
   if i%2 != 0:
      i += 1
      continue
   print(f"Try {i}")
   i += 1
   if i>=10:
      break
print("Stop Loop Ended")"""


"""i = 1
while i <= 5:
   print(i * " SP ")
   i += 1"""


"""i = 0
while i <= 5:
   x = 1
   while x<i:
      print(f" S P {i} ",end = "")
      x = x+1
   print("")
   i += 1"""
      
"""for i in range(6):
   print(f"S P {i} " * i)"""


"""#pwd = "1234"
trail = 1
while trail<=3:
    pin = input(f"Trail {trail} Enter Pin:").strip()
    trail += 1
    if pin == "1234":
        print("Correct")
        break
    else:
        print("Wrong!")"""  

"""for i in range(2,12,2):
    print(i,end = ",")"""

"""c = "suraj"
for index, char in enumerate(c):
    print(f"{char*index}")"""

"""for i in range(2,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")"""

"""l = [23,45,32,21,90]
dl = []
for i in l:
   dl.append(i*2)
   print(dl)"""
   

"""stud_info = {
    "name":"Suraj",
    "age":24,
    "marks":456,
    "city":"Sira"
}
for std, info in stud_info.items():
    print(f"{std} = {info}")"""

"""name = ["Suraj","vikas","Manu","Dinu"]
marks = [30,40,50,60]

student ={}

for index,var in enumerate(name):
    student[var] = marks[index]
print(student)"""


"""name = ["Suraj","vikas","Manu","Dinu"]
marks = [30,40,50,60]
student = {}

for i in range(len(name)):
   student[name[i]] = marks[i]
print(student)"""


"""names = ["Manu","Gudde","Sudeepa","Girish"]
d = {name:len(name) for name in names}
print(d)"""

"""city = {
    "Bangalore": 100,
    "Tumkur": 77,
    "Sira":59,
    "Mysore":34
}
#lc = {key:value for key,value in city.items() if value >=60}
lc = {uru:pop for uru,pop in city.items() if pop >=60}  
print(lc)"""


"""city = {
    "Bangalore": 100,
    "Tumkur": 77,
    "Sira":59,
    "Mysore":34
}
#lc = {key:value for key,value in city.items() if value >=60}
lc = {town:num for town,num in city.items() if num >=50}  
print(lc)"""

"""n = input("Enter list of names").split()
print(n)"""



"""#--------This is for Integers----------------
l = [int(num) for num in input("enter a list integers : ").split()]
print(l)"""



"""#--------This is String-----------------
l = [num for num in input("enter a list of names in the family : ").split()]
print(l)"""

"""i = 1
while i<=5:
    print(i,end = " ")
    i+=1"""
