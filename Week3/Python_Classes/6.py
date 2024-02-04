def Reverse(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

Sentence_input = input()
result = Reverse(Sentence_input)
print(Sentence_input)
print(result)