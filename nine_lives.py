import random
lives = 9 
words = ['fairy', 'teeth', 'shirt','otter','plane']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2665'
guess_word_correctly = False

def update_clue(guess_letter , secret_word, clue):
	index = 0
	while index < len(secret_word):
		if guess_letter == secret_word[index]:
			clue[index] = guess_letter
		index = index +1

def check_clue(clue):
	index = 0
	count = 0
	while index < len(clue):
		if clue[index] != '?':
			count = count + 1
		index  = index + 1
	return count

while lives > 0:
	print(clue)
	print('Lives Left: ' + heart_symbol * lives )
	print('Typing quit to exit! ')
	guess = input('Guess a letter or the whole word:')

	if guess == 'quit':
		break

	if guess == secret_word:
		guess_word_correctly = True
		break
    
	if guess in secret_word and len(guess) == 1:
		update_clue(guess, secret_word, clue)
	else:
		print('Incorrect. You lose a life')
		lives = lives - 1

	if check_clue(clue) == 5:
		guess_word_correctly = True
		break

if guess_word_correctly:
	print('You won! The correct word was ' + secret_word)
else:
	print('You lose! The correct word was '+ secret_word)