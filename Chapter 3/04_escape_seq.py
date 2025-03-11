# Escape Sequence in Python

a= "Urmi is a computer engineer\n Innovating the future"
print(a)

'''
\n is a newline character in Python, so it creates a line break between the two phrases. 
The string will be printed on two lines when you run the code.

## What is an Escape Sequence?
Escape sequence হলো একটি বিশেষ character combination যা string-এর মধ্যে কিছু নির্দিষ্ট কাজ বা আচরণ নির্দেশ করে।
Common Escape Sequences:

\n: Newline (line break)
\t: Tab (horizontal tab)
' : Single quote (')
" : Double quote (")
\r: Carriage return
\b: Backspace
\f: Form feed (page break)
'''

a= "Urmi is a computer engineer\t    Innovating the future"
print(a)


a= "Urmi is a computer engineer\r Innovating the future"
print(a)