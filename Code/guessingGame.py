secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while not(out_of_guesses) and guess != secret_word:
  if guess_count < guess_limit:
    guess = input('Enter guess: ')
    guess_count +=1
  else:
    out_of_guesses = True
  
if out_of_guesses:
  print('Out of guesses, YOU LOSE!')
else:  
  print(f'You win after {guess_count} try(ies)')