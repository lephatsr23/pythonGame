import random
lives = 9 
words_Easy = ['fairy', 'teeth', 'shirt','otter','plane']
words_Normal = ['cocacola', 'macdonal', 'circlek','lotteria','cinima']
words_Hard = ['hipopotamus', 'homolocu', 'Gastonia','camila','dinosaur','neoastrong']

difficulty = input('Choice difficulty (type 1, 2, or 3):\n 1) Easy\n 2) Normal\n 3) Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
	lives = 12
	secret_word = random.choice(words_Easy)
elif difficulty == 2:
	lives = 9
	secret_word = random.choice(words_Normal)
else:
	secret_word = random.choice(words_Hard)
	lives = 6

clue = list()
heart_symbol = u'\u2665'
guess_word_correctly = False

index = 0
while index < len(secret_word):
	clue.append('?')
	index = index + 1

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
		guess_word_correctly = 2
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

if guess_word_correctly == True:
	print('You won! The correct word was ' + secret_word)
elif guess_word_correctly == 2:
	print('You exit game')
else:
	print('You lose! The correct word was '+ secret_word)