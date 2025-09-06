# Problem 1

import math
print("*****Problem   1*****")
list = [1, 2, 3, 4, 5]
sum = 0

for i in list:
    sum += i
print(sum)
print(sum/len(list))
print()

# Problem 2

print("*****Problem   2*****")
celsius = 10
kelvin = celsius + 273.15
print(celsius, "C is converted to", kelvin, "K")
print()

# Problem 3

print("*****Problem   3*****")
word = ""
word += "racecar"
reverse_word = word[::-1]
if word == reverse_word:
    print("It is a Palindrome!")
else:
    print("It is not a Palindrome.")
print()

# Problem 4

print("*****Problem   4*****")
fruit = ""
fruit += "banana"
reverse_fruit = ""
for i in range(len(fruit) - 1, -1, -1):
    reverse_fruit += fruit[i]
print(reverse_fruit)
print()

# Problem 5

print("*****Problem   5*****")
list = ["Daniel", "Bernadette", "Dave", "Lily"]
names = ""
for i in range(len(list)):
    names += list[i] + " "
print(names)
print()

# Problem 6

print("*****Problem   6*****")
word = ""
word += "thinking"
is_pangram = True
pangram = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(pangram)):
    if word.find(pangram[i]) == -1:
        is_pangram = False

if is_pangram == True:
    print("This is a Pangram")
else:
    print("This is not a Pangram.")
print()

# Problem 7

print("*****Problem   7*****")
r = 125
Area = math.pi * (r ** 2)
Circumference = 2 * math.pi * r
print("Area: ", (Area))
print("Circumference: ", (Circumference))
print()

# Problem 8

print("*****Problem   8*****")
total_minutes = 873
hours = total_minutes // 60
print("Hours: ", (hours))
minutes = total_minutes % 60
print("Minutes: ", (minutes))
print()

# Problem 9

print("*****Problem   9*****")
word = "medicine"
count = 0
vowels = "aeiou"
for i in range(len(word)):
    if vowels.find(word[i]) == -1:
        count += 1
print("Number of Vowels: ", count)
print()

# Problem 10

print("*****Promblem 10*****")
number_check = 5
is_prime = True
for i in range(2, number_check):
    if number_check % i == 0:
        is_prime = False
if is_prime == True:
    print(number_check, "is a Prime Number!")
else:
    print(number_check, "is not a Prime Number.")
