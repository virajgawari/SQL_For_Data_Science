#02-JAN-2026

#Problem 1 :-

#To check if the given string is palindrome or not

text = input('Enter a text : ')
text = text.lower()  # Consistent output even if user enters uppercase letters 

reverse = text[::-1] # Here we reversed the string

if reverse == text:  # This is the logic to check if the string is palindrome or not
    print('Is palindrome')
else:
    print('Not a palindrome')


#Problem 2 :-

#To check if the given string is Anagram

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if len(word1) != len(word2):
    print('Not an anagram')
else:
    word2_list = list(word2)

    for i in word1:
        if i in word2_list:
            word2_list.remove(i)  
        else:
            print('Not an anagram')
            break
    else:
        print('Is an anagram')
