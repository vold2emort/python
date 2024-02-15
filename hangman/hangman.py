import random
from hangman_word import word_list
from hangman_art import logo, stages

display = []
lives = 6
choosen_word = random.choice(word_list)
print(f'the word is {choosen_word}.')
print(logo)
word_length = range(len(choosen_word))
# below is test line

for _ in word_length:   # len returns 0,1,2....
    display += '_'
print(display)
end_of_game = False
while not end_of_game:
    guess = input('Guess a word: - ').lower()
    if guess in display:
        print('you have already guessed the letter')
    for position in word_length:
        letter = choosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in choosen_word:
        print(f'the letter {guess} is not in the word, You lose a life')
        lives -= 1
        if lives == 0:
            print('you lose')
            end_of_game = True
    print(display)
    if '_' not in display:
        end_of_game = True
        print('you win')
    print(stages[lives])
