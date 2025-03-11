name=input ("Enter your name = ")
print ( f"Good Morning {name}")

# The f-string is used to format the string by inserting the name variable inside the greeting message.

letter= '''Dear <|Name|>
You are Selected !
<|Date|>
'''
print (letter.replace("<|Name|>","Urmi").replace("<|Date|>","2025"))

''' Replacing placeholders with actual values
print(letter.replace("<|Name|>", "Urmi").replace("<|Date|>", "2025")) '''