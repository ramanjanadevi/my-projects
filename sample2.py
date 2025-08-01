import random
words = ["apple", "tiger", "chair", "bread", "plant"]
word = random.choice(words)
hidden = ["_"] * len(word)
tries = 6
while tries > 0 and "_" in hidden:
    print("Word:", " ".join(hidden))
    guess = input("Guess a letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)
if "_" not in hidden:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
