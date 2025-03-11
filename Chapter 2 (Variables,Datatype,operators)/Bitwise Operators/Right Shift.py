# Bitwise Right Shift (>>)

a = 10      # বাইনারি: 1010
print(a >> 1)  # Output: 5 (0101)
print(a >> 2)  # Output: 2 (0010)


# Right Shift (>>) অপারেটরটি একটি সংখ্যার বাইনারি বিটগুলোকে ডানে সরিয়ে দেয় এবং
#  বাম পাশে 0 (শূন্য) যোগ করে।
'''

🔍 Explanation:
🔸 1-bit Right Shift:
a = 10 → 1010
a >> 1 → 0101 → 5 (Decimal)

🔸 2-bit Right Shift:
a = 10 → 1010
a >> 2 → 0010 → 2 (Decimal)'


📌 Shortcut Rule:
👉 a >> n = a // (2^n)

a >> 1 = a // 2
a >> 2 = a // 4
a >> 3 = a // 8

'''