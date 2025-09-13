# Problem 1

print("*****Problem  1*****")
length = 6
width = 17
area = (length * width)
print(area)
print()

# Problem 2

print("*****Problem  2*****")
name = "Lily"
age = 22
message = "Hello! My name is {} and I am {} years old"
print(message.format(name, age))
print()

# Problem 3

print("*****Problem  3*****")
number = 6
if number % 2 == 0:
    print("The number is Even!")
else:
    print("The number is odd.")
print()

print("*****Problem  4*****")
list = [7, 14, 24, 38, 81]
print(min(list))
print(max(list))
print()

print("*****Problem  5*****")
word = "mom"
reverse_word = word[::-1]
print(word)
if word == reverse_word:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")
print()

print("*****Problem  6*****")
P = 1500
r = 0.06
n = 12
t = 4
A = P * (1 + r/n)**(n*t)
CI = A - P

print("The compound interest is:", (f"{CI:.2f}"))
print()

print("*****Problem  7*****")
days = 489
years = (days // 365)
days_remaining = days % 365
weeks = days_remaining // 7
days_left = days_remaining % 7

time = ("Years: {}, Weeks: {}, Days: {}")
print(time.format(years, weeks, days_left))
print()

print("*****Problem 8*****")
numbers = [5, 8, -9, 7, -15, 25, -10]
positive_sum = 0
for num in numbers:
    if num > 0:
        positive_sum += num
print("The sum of all positive numbers is", positive_sum)
print()

print("*****Problem  9*****")
sentence = "Today is Warm and Sunny"
words = sentence.split()
count = len(words)
print("The number of words in the sentence is", count)
print()

print("*****Problem 10*****")
one = 10
two = 7

print(
    f"Before swapping: Variable one: {one}   and Variable two: {two}")
one, two = two, one
print(f"After swapping: Vriable one: {one}  and Variable two: {two}")
