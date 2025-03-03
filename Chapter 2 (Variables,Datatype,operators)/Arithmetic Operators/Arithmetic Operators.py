#  + - * / // **
# Addition and Unary Plus Operator (+)
# Subtraction or Unary Minus Operator (-)
# Multiplication Operator (*)
# Division Operator (/)
# Floor Division Operator (//)
# Modulus Operator (%)
# Power Operator (**)


# Addition and Unary Plus Operator (+)
x= -10
y= +(x)
print (y)
#result -10 

# Subtraction or Unary Minus Operator (-)
x= -10
y= -(x)
print (y)
# result 10

# Unary Minus শুধু সাইন পরিবর্তন করে, সংখ্যাকে গুণিতক বা ডাবল করে না।
# x = -10 হলে -(x) মানে -(-10) হয়ে যাবে +10, কিন্তু এটা কখনোই 20 হবে না।
# Unary Minus (-) শুধু সাইন পরিবর্তন করে।
# Unary Plus (+) কোনো সাইন পরিবর্তন করে না, তবে এটা সঠিকভাবে সংখ্যাকে পজিটিভ হিসেবে প্রকাশ করতে সাহায্য করে, যদিও এটি সাধারণত অপরিহার্য নয়।

# Multiplication Operator (*)
x=20
y=8
print (x*y)

# Division Operator (/)
x=10
y=20
print (x/y)

#another
x=20
y=10
print (x/y)

# Division (/) অপারেটর দুটি সংখ্যাকে ভাগ করে এবং float (ফ্লোট) মান (যেমন ০.৫) প্রদান করে।


# Floor Division Operator (//)
x=35
y=2
print (x//y)

# এখানে:
# x = 35 এবং y = 2।
# 35 ÷ 2 এর ফলাফল হবে 17.5।
# কিন্তু Floor Division অপারেটর // দশমিক অংশ (0.5) বাদ দিয়ে ফলস্বরূপের পূর্ণসংখ্যা (integer) রিটার্ন করবে।
# এটি Division (/) অপারেটর থেকে আলাদা, কারণ / অপারেটর ফ্লোট মান (যেমন, 17.5) রিটার্ন করে, কিন্তু // শুধুমাত্র পূর্ণসংখ্যা প্রদান করে।

# Modulus Operator (%)
x=4
y=2
print (x%y)

# result=0
# Modulus (%) অপারেটর দুটি সংখ্যার মধ্যে ভাগফল থেকে বাকি অংশ বের করে।
# এখানে, x = 4 এবং y = 2।
# 4 ÷ 2 এর ভাগফল 2 হবে এবং বাকিটুকু (remainder) 0 থাকবে, কারণ 4 কে 2 দিয়ে ভাগ করলে কোনো বাকি অংশ থাকে না।
# অর্থাৎ:

# x % y মানে 4 % 2 হবে 0, কারণ 4 কে 2 দিয়ে ভাগ করলে কোনো বাকি থাকে না।

x=5
y=2
print (x%y)

# result=1
# Modulus (%) অপারেটর দুটি সংখ্যার মধ্যে ভাগফল থেকে বাকিটুকু (remainder) রিটার্ন করে।
# যেমন, 5 % 2 এর ফলাফল হবে 1, কারণ 5 কে 2 দিয়ে ভাগ করলে 1 বাকি থাকে।

# Power Operator (**)
x=31
y=4

print(x**y)

# এই অপারেটরটি x^y হিসেবে কাজ করে।
# x ** y মানে 31 কে 4 বার গুণ করা।
# 31 ** 4 এর মান হবে 31 × 31 × 31 × 31 = 923521

