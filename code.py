import random
# 2d list with words and their corresponding descritpors
words = [['greeting','python','table','create','script','stethoscope','hedgehog','accelerate','xylophone','circle'],
['some act of communication','a digital snake','has a flat top','to design from scratch','a kind of blueprint',
'doctors like it','spiny mammal','to move faster','musical instrument','ever closed']];
num_of_words = len(words[0])
play = True
while play:
game_over = False
index = random.randint(0,num_of_words-1) # generating random integer between 0 and 9
word_to_guess = words[0][index]
number_of_letters_in_word = len(word_to_guess)
print('Guess the word based on this clue: ')
for i in range(number_of_letters_in_word): # generate clue
show = random.random();
hide = random.random();
  
if show>hide:
print(word_to_guess[i],end = '') # print letter in the word
else:
print('-',end = '') # hide letter and print dash
print('\n[',words[1][index],']') # show the descriptor   
#playing starts
passed = False
has_chances = True
max_rounds = 5
rounds = 1
while not passed and has_chances:
print('\nChances remaining: ',max_rounds-rounds+1)
guess = input('Enter your guess: ')
if guess==word_to_guess:
print('Congratulations!')
game_over = True
passed = True
play = False
rounds = rounds+1
has_chances = rounds<=max_rounds
if not passed:
print('failed!')
if not game_over:
play = (input('keep playing? y/n: ')=='y')
