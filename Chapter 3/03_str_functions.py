name="urmi"
print(len(name))
# len(name)	string এর মোট character সংখ্যা দেখায়

print(name.endswith("mi"))
# endswith("mi") → Checks if the string ends with "mi" → True

print(name.startswith("ur"))
# startswith("ur") → Checks if the string starts with "ur" → True

print(name.capitalize())
# capitalize() → Converts first letter to uppercase → "Urmi"

print(name.lower())         # Output: "urmi" → Converts to lowercase → "urmi"
print(name.upper())         # Output: "URMI" → Converts to uppercase → "URMI
print(name.replace("ur", "UR")) # Output: "URmi" → Replaces 'ur' with 'UR' → "URmi"
print(name.strip())         # Output: "urmi" → Removes extra whitespace → "urmi"
print(name.split())         # Output: ['urmi'] → Splits the string by spaces → ['urmi']
print(" ".join(['Hello', 'world']))  # Output: "Hello world" →
print(name.find("mi"))       # Output: 2 → Finds index of 'mi' → 2
print(name.count("ur"))      # Output: 1 → Counts occurrences of 'ur' → 1
print("1234".isdigit())      # Output: True → Checks if all characters are digits → True
print(name.isalpha())        # Output: True → Checks if all characters are alphabets → True


'''
Syntax: name.function(parameter)
Explanation:
name: The string or object working with (e.g., "urmi").
    .: The dot operator used to call the method.
function: The method you're calling (e.g., upper(), replace()).
parameter: The argument you pass to the method (if required)

''' 