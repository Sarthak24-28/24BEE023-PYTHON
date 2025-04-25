class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def __str__(self):
        return self.value

str1 = String("Hello")
str2 = String(" World")

str1 += str2
print("After concatenation:",str1)

str1.toLower()
print("After converting to lowercase:",str1)

str1.toUpper()
print("After converting to uppercase:",str1)
