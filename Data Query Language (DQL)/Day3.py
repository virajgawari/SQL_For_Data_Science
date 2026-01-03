# 03-JAN-2026

# Problem 1 :-

# Character Frequency Counter

text = input("Enter a string: ")

frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for key, value in frequency.items():
    print(key, ":", value)


# Problem 2 :-

# Write a program that takes a string and prints the first character that does NOT repeat.

text = input("Enter a string: ")

frequency = {}

for i in text:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

found = False

for i in text:
    if frequency[i] == 1:
        print("First non-repeating character:", i)
        found = True
        break

if not found:
    print("No unique character")
