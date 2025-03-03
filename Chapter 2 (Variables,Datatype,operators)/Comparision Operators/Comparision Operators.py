a = 15
b = 10

print(a > b)   # Greater than
print(a < b)   # Less than
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to



# ==	Equal to	5 == 5	True
# !=	Not Equal	5 != 3	True
# >	Greater than	10 > 3	True
# <	Less than	3 < 5	True
# >=	Greater than or equal to	10 >= 10	True
# <=	Less than or equal to	5 <= 7	True

# List of Comparison Operators in Python
# Greater than (>)
# Less than (<)
# Equal to (==)
# Not equal to (!=)
# Greater than or equal to (>=)
# Less than or equal to (<=)


a= 20<=10
print(a)


print(3.55 == 3.55)  #true
print (20>=10)   #true

print (10!=20)  #true 
print(3.55 != 3.55)  #false



x='apple'
y='apricot'
print (x>=y) #false

# How it Works:
# In Python, comparison operators like >= can be used to compare strings.

# 👉 When comparing strings, Python compares their ASCII values (Letter by Letter).

# How the Comparison Happens:
# The first letter of x → 'apple' → a (ASCII = 97)
# The first letter of y → 'apricot' → a (ASCII = 97)
# Since the first letters are equal, Python checks the second letter:

# Second letter in 'apple' → p (ASCII = 112)
# Second letter in 'apricot' → p (ASCII = 112)
# They are equal again! ✅

# Now Python checks the third letter:

# Third letter in 'apple' → p (ASCII = 112)
# Third letter in 'apricot' → r (ASCII = 114)
# Result:
# 👉 Since p is smaller than r, the condition apple >= apricot will return:False


# Important Rule:
# Python compares strings alphabetically.
# The comparison is Case-Sensitive.
# Small letters (a-z) have higher ASCII values than capital letters (A-Z).
# What is ASCII = 112?
# 🔥 ASCII Full Form: American Standard Code for Information Interchange

print(4>6 == False)


print (True==True==False)