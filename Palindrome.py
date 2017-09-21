#PALINDROME

print("ENTER MIN OF 3 LETTERS")
word = input()

word = word.casefold()

rev_word = reversed(word)

if list(word) == list(rev_word):
   print("IT IS PALINDROME")
else:
   print("NOT PALINDROME")