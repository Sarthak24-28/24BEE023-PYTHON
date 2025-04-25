def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if ispalindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
