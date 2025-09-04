def count_words(sentence):
    return len(sentence.split())

# User input
sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))
