print("This is a plaindrome checker")
word = input("Enter your word here: ")

reversed = word[::-1]

if word == reversed:
    print(word + " is a palindrome!")
else:
    print(word + " is not a palindrome!")