def ispangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    sentence_letters = set(sentence.lower())
    
    return alphabet <= sentence_letters

test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Crazy Fredrick bought many very exquisite opal jewels"
test3 = "This sentence is not a pangram"

print("Test 1:",test1)
print(ispangram(test1))

print("\nTest 2:",test2)
print(ispangram(test2))

print("\nTest 3:",test3)
print(ispangram(test3))
