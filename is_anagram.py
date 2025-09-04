def is_anagram(s, t):
    return sorted(s) == sorted(t)

# User input
s = input("Enter first string: ")
t = input("Enter second string: ")

if is_anagram(s, t):
    print("True")
else:
    print("False")
