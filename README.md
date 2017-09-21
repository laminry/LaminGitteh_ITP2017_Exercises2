# palindrome

print("ENTER MIN OF 3 LETTERS")

word = input() <br>
word = word.casefold() <br>
rev_word = reversed(word)<br>

if list(word) == list(rev_word):<br>
   print("IT IS PALINDROME")<br>
   
else:<br>
   print("NOT PALINDROME")<br>
