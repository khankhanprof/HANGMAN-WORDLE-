import random 
from hangman_art import stages 
from hangman_art import logo
from hangman_words import word_list
#user friendy welcome message
print("welcome to the game ")
print(logo)
#choose random word from word_list
chosen_word=random.choice(word_list)
print(chosen_word)
#make a mock list and replace all the letters to dashes 
display=[]
for i in range(0,len(chosen_word)):
  display.append("_")
#life=6 because the hangman game ends after 6 turns
life=6
value=True
while value:

  guess=input("guess a letter : ").lower()
  if guess in display:
      print("you already tried the letter, enter new letter")
  for i in range(0,len(chosen_word)):
    if chosen_word[i]==guess:
      display[i]=chosen_word[i]
  if guess not in chosen_word:
      if life==0:
        value=False
        print("you lose")
        break
      else:
        life-=1
        print(stages[life])
        
if "_" not in display:
  print("you win")
  print("".join(display))