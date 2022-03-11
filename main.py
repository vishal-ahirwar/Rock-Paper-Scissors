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

print("Welcome to Rack Paper Secissors Game\nLet's see who wins\n")
user_input=int(input("What do you choose ???\nType:\n0 =Rock\n1 =Paper\n2 =Secissors"))
from random import randrange

computer_choices=[ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
 '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
 '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

com_c=randrange(0,len(computer_choices)-1)
print("\nuser : "+computer_choices[user_input])
print("\ncomputer : "+computer_choices[com_c])

if user_input==com_c:
    print("Who won I don't know....")
elif user_input==0 and com_c==2:
    print("user won!:)")
elif user_input==2 and com_c==0:
    print("computer won!:)")
elif com_c>user_input:
    print("Computer won! ;(")
elif user_input>=3 or user_input<0:
    print("invalid option!")
elif user_input>com_c:
    print("user won! :)")
else:
    print("well!!!!!!!!!!!!!! ....")


