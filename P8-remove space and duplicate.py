def convert(input_string):
    words = input_string.split()
    
    unique_words = set(words)
    
    sorted_words = sorted(unique_words)
    
    return ' '.join(sorted_words)

input_string = input("Enter a sequence of words: ")
result = convert(input_string)

print("Result after removing duplicates and sorting:", result)
