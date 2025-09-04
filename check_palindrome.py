def check_palindrome(word):
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

# User input
text = input("Enter a word: ")

if check_palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
