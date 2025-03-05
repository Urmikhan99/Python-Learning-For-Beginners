
#Bitwise AND(&)
#Returns 1 if both bits are 1, else it returns 0.


a=10
b=5
print (a&b)    
#result=0


'''
এখানে & হলো Bitwise AND Operator
এই অপারেটরটি বাইনারি সংখ্যার Bitwise AND অপারেশন করে।
Bitwise AND মানে দুটি সংখ্যার প্রতিটি বিটকে তুলনা করা হয়,
এবং যদি দুই বিটই 1 (True) হয়, তাহলে রেজাল্ট 1 হবে, নাহলে 0 হবে।

 সংখ্যা গুলোকে প্রথমে বাইনারি তে রূপান্তর করি:
a = 10 → 1010
b = 5 → 0101 
------------

   1010   → 10
&  0101   → 5
---------------
   0000   → 0

'''

a=65554455
b=5433353
print (a&b)


a=10
b=5
result= a & b
print= (bin (result))

#🔍 bin() Function in Python (Bangla)
'''✅ bin() হল Python-এর একটি বিল্ট-ইন ফাংশন, 
যা কোনো সংখ্যাকে (integer) বাইনারি (binary) ফরম্যাটে রূপান্তর করে।'''


'''
🎯 AND অপারেশন:
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1


✅ নিয়ম:
👉 দুই বিটই 1 হলে ফলাফল হবে 1
👉 একটি হলেও 0 থাকলে ফলাফল হবে 0
'''