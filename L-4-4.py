#L-4-4

num = int(input("Enter a number: "))


is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break


sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i
is_perfect = (sum_divisors == num)


temp = num
armstrong_sum = 0


digit_count = 0
temp_count = temp
while temp_count > 0:
    digit_count += 1
    temp_count //= 10


temp = num
while temp > 0:
    digit = temp % 10
    power = 1
    for _ in range(digit_count):
        power *= digit
    armstrong_sum += power
    temp //= 10

is_armstrong = (armstrong_sum == num)


original = num
reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

is_palindrome = (original == reversed_num)


square = num * num


is_automorphic = True
temp_num = num
temp_square = square

while temp_num > 0:
    if (temp_num % 10) != (temp_square % 10):
        is_automorphic = False
        break
    temp_num //= 10
    temp_square //= 10


print("\nResults:")
print("Prime:", is_prime)
print("Perfect:", is_perfect)
print("Armstrong:", is_armstrong)
print("Palindrome:", is_palindrome)
print("Automorphic:", is_automorphic)
