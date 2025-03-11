name="Urmi"
print(name[-4:-1])
print(name[1:4])


print(name[:4])
# শুরু থেকে index 4 এর আগ পর্যন্ত সব কিছু → index 0,1,2,3 → U, r, m, i
# name[:4] → start to index 3

print(name[1:])
# name[1:] → index 1 to end → 'rmi'
print(name[1:5])
# name[1:5] → index 1 to 4 (but string ends at 3) → 'rmi'
'''
Positive Index:  0   1   2   3
Characters:      U   r   m   i

Negative Index: -4  -3  -2  -1
Characters:      U   r   m   i
'''