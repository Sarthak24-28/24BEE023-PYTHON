def count_vowels(s, index=0):
    if index == len(s):
        return 0
    
    vowels = 'aeiouAEIOU'
    count = 1 if s[index] in vowels else 0
    
    return count + count_vowels(s, index + 1)

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels in the string:",vowel_count)
