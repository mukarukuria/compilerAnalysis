def split(sentence):
    words = sentence.split()
    return words

input_sentence = input("Enter an English sentence: ")

words = split(input_sentence)
for word in words:
    print(word)