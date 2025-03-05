# BITWISE NOT (~)

# Return one's Component of a Number


a=53
print(~a)



'''

Bitwise NOT (~) Explanation for a = 53

Step-by-Step Explanation:
a = 53
53 এর বাইনারি রূপ: 110101
1's complement (প্রতিটি বিটের বিপরীত করা):

110101 → 001010
2's complement (1 যোগ করা):

001010 + 1 → 001011
Final result:  ~53 = -54



Bitwise NOT (~) অপারেটর একটি সংখ্যার সকল বিটের বিপরীত রূপ তৈরি করে এবং 
2's complement পদ্ধতি অনুসরণ করে।
উদাহরণস্বরূপ, ~10 = -11।
'''


a= -53
print(~a)

# 52


'''
মনে রাখার ট্রিক 🎯:
"NOT মানে যা দেখবে, তার উল্টোটা করবে!"
👉 NOT মানে সবকিছু উল্টে দেওয়া (না মানে না!)

ব্যাখ্যা 💡:
Python-এ NOT অপারেটর শুধু উল্টায় না, বরং 2's Complement হিসাবেও কাজ করে।
👉 ধরা যাক 5 = 0101
👉 NOT চালালে হয় 1010 (উল্টো)
👉 এটাকে Decimal এ আনলে হয় -6
'''