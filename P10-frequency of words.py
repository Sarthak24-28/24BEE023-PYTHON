def frequency(s):
    words = s.split()
    
    word_freq = {}
    
    for word in words:
        word = word.lower()  
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    sorted_word_freq = dict(sorted(word_freq.items()))
    return sorted_word_freq

input_string = input("Enter a string: ")
result = frequency(input_string)

print("Word frequencies in sorted order:", result)
