# ✅ Types of Logical Operators in Python:  
# 1. **and** (Logical AND)  
# 2. **or** (Logical OR)  
# 3. **not** (Logical NOT)  

#1.Logical AND (and)
x=20
y=30
z=40

if x >y and y >z :
    print("x is the Largest Number")
else :
    print ("x is smaller number")
#x is smaller number

p=53466
g=4234345
h=2434443

if p<h and h>g:
    print ("h is large number")
else:
    print ("h is small number")
#h is small number
#যেহেতু and অপারেটর ব্যবহৃত হয়েছে, শর্ত দুটি দুইটি সত্য হওয়া প্রয়োজন। কিন্তু এখানে দ্বিতীয় শর্তটি মিথ্যা (False) হওয়ায়, পুরো শর্তটি False হবে।


#Logical OR(or)
a=40
b=80
c=10
if a>b or a>c:
    print ("a is bigger than one number")
else:
    print ("a is smaller number")
#a is bigger than one number

# এখন, যেহেতু or অপারেটর ব্যবহার করা হয়েছে, শর্তগুলির মধ্যে একটি শর্তও সত্য হলে পুরো শর্তটি সত্য হবে। এখানে দ্বিতীয় শর্তটি সত্য (True), তাই পুরো শর্তটি True হবে।

#or
age =15
income=20000
if age>18 or income >=1500:
    print ("eligible for the loan")
else:
    print("Not eligible")
#eligible for the loan

#and logic
age =15
income=20000
if age>18 and income >=1500:
    print ("eligible for the loan")
else:
    print("Not eligible")
#not eligible


# 3.Logical NOT(not)
x=10
y=20
z=30
if not (x>y or x>z):
    print("x is not largest Number")
else:
    print("x is not largest Number")
#x is not largest Number

#and ,not
x=5
y=10
z=20
print(x<y and not z>30)