import random

word_bank = ['python' , 'javascript' , 'java' , 'rust' , 'go' , 'html' , 'sql' , 'php' , 'ruby']
word = random.choice(word_bank)
guessedword = ['_']*len(word)
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedword))

  guess = input('Guess a letter: ').lower()

  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedword[i] = guess
            print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedword:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedword:
  print('\nYou\'ve run out of attempts! The word was: ' + word)
