***Decimal to Binary and Binary to Decimal Conversion***
Introduction to Number System

• Represents a quantity through a set of numbers.

Types of Number Systems:

1. Decimal (Base 10)

2. Binary (Base 2)

3. Octal (Base 8)

4. Hexadecimal (Base 16)




***Bitwise Operators in Python - Notes***
Bitwise operators are used to perform operations on binary numbers (bits). In Python, these operators work on the bit level of integers. Python provides several bitwise operators to perform operations on bits.

List of Bitwise Operators:

Bitwise AND (&)

The AND operator compares the corresponding bits of two numbers and returns 1 if both bits are 1, otherwise it returns 0.
Example: a & b

a = 10  # 1010
b = 5   # 0101
result = a & b  # 0000 -> 0
print(result)


Bitwise OR (|)
The OR operator compares the corresponding bits of two numbers and returns 1 if at least one of the bits is 1, otherwise it returns 0.
Example: a | b

a = 10  # 1010
b = 5   # 0101
result = a | b  # 1111 -> 15
print(result)


Bitwise XOR (^)
The XOR operator compares the corresponding bits of two numbers and returns 1 if the bits are different; otherwise, it returns 0.
Example: a ^ b

a = 10  # 1010
b = 5   # 0101
result = a ^ b  # 1111 -> 15
print(result)

Bitwise NOT (~)
The NOT operator inverts all the bits of the number, changing 1 to 0 and 0 to 1. It’s equivalent to taking the 2's complement of the number.
Example: ~a



a = 53  # 110101
result = ~a  # -54 (in 2's complement)
print(result)


Left Shift (<<)
The Left Shift operator shifts the bits of the number to the left by a specified number of positions, and fills the empty positions with 0. This is equivalent to multiplying the number by 2 for each shift.
Example: a << n (shift a by n positions to the left)


a = 5  # 0101
result = a << 1  # 1010 -> 10
print(result)
Right Shift (>>)

The Right Shift operator shifts the bits of the number to the right by a specified number of positions, and fills the empty positions with the sign bit (either 0 for positive numbers or 1 for negative numbers).
 This is equivalent to dividing the number by 2 for each shift.
Example: a >> n (shift a by n positions to the right)

a = 10  # 1010
result = a >> 1  # 0101 -> 5
print(result)
Example Code for All Bitwise Operators:


a = 10  # 1010
b = 5   # 0101

# AND Operation
print("a & b =", a & b)  # Output: 0

# OR Operation
print("a | b =", a | b)  # Output: 15

# XOR Operation
print("a ^ b =", a ^ b)  # Output: 15

# NOT Operation
print("~a =", ~a)  # Output: -11

# Left Shift
print("a << 1 =", a << 1)  # Output: 20

# Right Shift
print("a >> 1 =", a >> 1)  # Output: 5


Summary:
Bitwise AND (&): Returns 1 if both bits are 1.
Bitwise OR (|): Returns 1 if either bit is 1.
Bitwise XOR (^): Returns 1 if the bits are different.
Bitwise NOT (~): Inverts all bits (1 becomes 0, and 0 becomes 1).
Left Shift (<<): Shifts bits to the left, multiplying by powers of 2.
Right Shift (>>): Shifts bits to the right, dividing by powers of 2.
Important Points:
Bitwise operators work at the binary level of numbers.
They are commonly used in low-level programming like system programming, encryption algorithms, and in situations where we need to manipulate specific bits.

-----------------------------------------------------------

🔥 ***Python Bitwise Operators Notes***

# Bitwise Operators in Python

Python-এ Bitwise Operators বাইনারি সংখ্যার উপর সরাসরি কাজ করে।

| Operator | Name        | Description                             |
|----------|-------------|-----------------------------------------|
| &        | AND         | দুই বিটই 1 হলে 1, নাহলে 0              |
| \|       | OR          | কমপক্ষে একটি বিট 1 হলে 1               |
| ^        | XOR         | দুই বিট ভিন্ন হলে 1, একই হলে 0        |
| ~        | NOT         | প্রতিটি বিট উল্টে দেয় (1 কে 0, 0 কে 1) |
| <<       | Left Shift  | নির্দিষ্ট সংখ্যক বিট বামে সরিয়ে দেয়   |
| >>       | Right Shift | নির্দিষ্ট সংখ্যক বিট ডানে সরিয়ে দেয়  |

## Explanation
Bitwise অপারেটর গুলি ডেটা এনক্রিপশন, ফাইল কম্প্রেশন এবং লো লেভেল প্রোগ্রামিং-এ ব্যবহার করা হয়। এগুলি বিভিন্ন ধরণের অপারেশন যেমন বিট যোগ, বিট শিফট, এবং বিট কমপ্লিমেন্ট সহ আরো অনেক কিছু করে থাকে।

## Bitwise Operators Examples

### 1. Bitwise AND (&)
👉 **নিয়ম:**  

দুই বিটই 1 হলে ফলাফল হবে 1, নাহলে 0।

```python
a = 5  # 0101
b = 3  # 0011
result = a & b
print("AND:", result)  # Output: 1


2. Bitwise OR (|)
👉 নিয়ম:
যদি কমপক্ষে একটি বিট 1 হয়, তাহলে ফলাফল হবে 1।

a = 5  # 0101
b = 3  # 0011
result = a | b
print("OR:", result)  # Output: 7


 3. Bitwise XOR (^) 
👉 নিয়ম:
যদি দুই বিট ভিন্ন হয়, তাহলে ফলাফল হবে 1। যদি একই হয়, তাহলে ফলাফল হবে 0।

a = 5  # 0101
b = 3  # 0011
result = a ^ b
print("XOR:", result)  # Output: 6


4. Bitwise NOT (~)
👉 নিয়ম:
প্রতিটি বিট উল্টে দেয়।
Python-এ এটি Two's Complement ব্যবহার করে।
a = 5  # 0101
result = ~a
print("NOT a:", result)  # Output: -6



5. Bitwise Left Shift (<<)
👉 নিয়ম:
বিটগুলোকে বামে সরিয়ে দেয় এবং শূন্য (0) যোগ করে।
a = 5  # 0101
result = a << 1
print("Left Shift a:", result)  # Output: 10


6. Bitwise Right Shift (>>)
👉 নিয়ম:
বিটগুলোকে ডানে সরিয়ে দেয় এবং শূন্য (0) যোগ করে।
a = 5  # 0101
result = a >> 1
print("Right Shift a:", result)  # Output: 2


AND: 1
OR: 7
XOR: 6
NOT a: -6
Left Shift a: 10
Right Shift a: 2



Conclusion
Python Bitwise Operators গুলি ডেটা ম্যানিপুলেশনের জন্য খুবই গুরুত্বপূর্ণ।