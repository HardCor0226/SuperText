import time

#Possible User Responses
answer_A = ['A', 'a']
answer_B = ['B', 'b']
answer_C = ['C', 'c']
answer_D = ['D', 'd']
yes = ['Y', 'y', 'yes']
no = ['N', 'n', 'no']

#Possible Inventory Items
costume = 0
sword = 0
health_potion = 0

required = ('\nUse only A, B, or C\n')

def start_screen():
    print ('Welcome to Super Text! Press "Enter" to begin!')
    choice = input('')
    if (len(choice) < 1):
        pass
    else:
        print('Please press "Enter" to begin!')
        start_screen()


start_screen()
time.sleep(2)
print('What is your name, stranger?')
name = input('Enter name:')
time.sleep(2)

def intro():
    print('Hello',name + '!', 'After a storm decimated your entire village, you and the three other survivors took all that you'
            ' had left and began a journey to find your new home. After an hour of trekking through the forest, eight year-old Maura began'
            ' to complain about her feet hurting. She always looked to you as an older sibling and often depended on you for help.'
            ' You contemplated what you should do...')
    time.sleep(2)
    print('A. Pick up Maura and carry her on your back'
            '\nB. Tell Maura to stop complaining and be strong'
            '\nC. Ignore and keep walking. You are in no mood for weakness.')
    choice = input('>>>' )
    if choice in answer_A:
        option_carry()
    elif choice in answer_B:
        option_beStrong()
    elif choice in answer_C:
        print('\nBecause of your cold hearted decision, you did not realize Maura was close to falling unconscious.'
            ' Maura ended up passing out while walking near a cliffside and fell to her death! Angered by your decision,'
            ' the rest of the group turned on you and threw you over, as well! \n\nYOU DIED')
    else:
        print(required)
        intro()

def option_carry():
    print('Maura laughs with joy as you lift her up onto your back. You all continue walking for a few more hours until'
    ' you notice the sun begin to set. You hear the others start murmuring about wanting to set up camp for the night.'
    ' Will you:')
    time.sleep(2)
    print('A. Set up Camp'
    '\nB. Ignore the others and continue to walk through the night')
    choice = input('>>>' )
    if choice in answer_A:
        option_rest()
    elif choice in answer_B:
        print('\nBecause of your terrible decision, the whole group dies after a run in with a bear because they were all'
        'too exhausted to escape it. The bear saves you for last. \nYOU DIED')
    else:
        print(required)

intro()
