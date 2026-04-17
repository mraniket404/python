dictionary = {
    "madat": "help",
    "pyar": "love",
    "dost": "friend",
    "mohabbat": "romance"
}
word = input("Enter a word: ")

if word in dictionary:
    print(f"The meaning of '{word}' is: {dictionary[word]}")
else:
    print(f"'{word}' is not in the dictionary.")
