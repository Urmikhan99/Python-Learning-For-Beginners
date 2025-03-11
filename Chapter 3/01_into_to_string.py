name="urmi"
nameshort = len(name)
print (nameshort)

# Explanation:

# len() returns the number of characters in a string.
# "urmi" has 4 characters, so len("urmi") is 4.

name="shormi"
nameshort = name[0:3] #start form index 0
print (nameshort)
"""
name[0:3] slices the string from index 0 up to (but not including) index 3.
So, it takes 's', 'h', 'o' → makes "sho"
"""


character1=name[1]
print(character1)

'''
Python-এ string এর প্রতিটি character-এর একটা করে index (ক্রম) থাকে।

Indexing 0 থেকে শুরু হয়, মানে:
Index:    0   1   2   3   4   5
Letter:   s   h   o   r   m   i
name[1] মানে হলো: name স্ট্রিং এর index 1 তে থাকা character টা, যা হলো 'h'

শেষ character, তখন name[-1] ব্যবহার করা যায় (negative indexing)।
'''