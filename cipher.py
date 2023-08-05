sentence = input("Please enter a plain text sentence: ")
sentence = sentence.lower()

cipher = {"a": "f", "b": "g", "c": "h", "d": "i", "e": "j", "f": "k", "g": "l", 
          "h": "m", "i": "n", "j": "o", "k": "p", "l": "q", "m": "r", "n": "s", 
          "o": "t", "p": "u", "q": "v", "r": "w", "s": "x", "t": "y", "u": "z", 
          "v": "a", "w": "b", "x": "c", "y": "d", "z": "e"}

new_sentence = ""
for letter in sentence:
    if letter in cipher:
        new_sentence += cipher[letter]
    else:
        new_sentence += letter

print(new_sentence)