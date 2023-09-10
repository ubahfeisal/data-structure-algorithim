import string
def word_frequency(sentence):
    word_freq = {}
    
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).lower().split()
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Test
sentence = "ubah feisal Moringa"
result = word_frequency(sentence)
print(result)