#  Palindrom (słowo brzmiące tak samo, kiedy czytane od tyłu)
# kajak
# civic
# Elf układał kufle
# A to kanapa pana kota


# # 3 formy range'a:
# range(100) # [0, 100)
# range(90, 100) # [90, 100)
# range(90, 100, 2) # [90, 92, 94, 96, 98]


# Palindrome checker

word = input("Please enter a word: ")
reverse_word = word[::-1]

if word == reverse_word:
    print(word, "is a palindrome")
else:
    print(word, "isn't a palindrome")

# # Version with "for"

# word = input("Please enter a word: ")
# if_palindrom = True # or False

# for i in range(len(word)):
#     if word[i] != word[-i -1]:
#         if_palindrom = False
#         break