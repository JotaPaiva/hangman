import random
import hangman_words
import hangman_arts

print(hangman_arts.intro)

lives = 6

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""

chosen_word_len = len(chosen_word)
for letter in range(chosen_word_len):
    placeholder += "_"

print("Word: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1

    print("\n" + display)
    print(hangman_arts.stages[lives])
    print(f"{lives} LIVES LEFT!")
    print("=========")

    if "_" not in display:
        game_over = True
        print("You win!")
        print("=========")
    elif lives == 0:
        game_over = True
        print("You lose!")
        print("=========")
