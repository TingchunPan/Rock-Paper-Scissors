rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
computer=[rock, paper, scissors]
computer_choice=random.choice(computer)
human_choices=[rock, paper, scissors]

human_choice_number=int(input('Please type the number 1 to 3 to play the game.\n1=rock, 2=paper, and 3=scissors \n'))

try:
 human_choice=human_choices[human_choice_number-1]
 if human_choice_number>3 or human_choice_number<0:
   print('Invalid typing.')
 else:
   print(f'Your choice: {human_choice}')
   print(f'Computer\'s choice: {computer_choice}')
   if computer_choice==human_choice:
     print(f'Your choice is the same as the computer\'s choice, so you draw.')
   elif computer_choice==rock and human_choice==paper:
    print('You win.')
   elif computer_choice==paper and human_choice==rock:
    print('You lose.')
   elif computer_choice ==scissors and human_choice == rock:
    print('You win.')
   elif computer_choice ==rock and human_choice == scissors:
    print('You lose.')
   elif computer_choice ==scissors and human_choice == paper:
    print('You lose.')
   elif computer_choice ==paper and human_choice == scissors:
    print('You win.')

except:
  print('Invalid typing.')