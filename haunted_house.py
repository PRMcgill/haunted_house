def prompt():
    print('What door do you choose? \n'
        'Door 1 \n'
        'Door 2 \n'
        'Door 3 \n'
        'Door 4 \n'
        'Door 5 \n'
        'Door 6 \n'
        'Door 7 \n'
        'Door 8 \n'
        'Door 9 \n'
        'Door 10 \n'
        'Door 11 \n'
            )
def make_choice():
    monster = ['Ghoul', 'Ghost', 'Cyclop', 'Zombie']

    doors = int(options)

    if doors > 11 or doors < 1:
        print('You ran into the wall. Pick a door. \n')
    elif doors % 2 == 0:
        print('Boo! You have been scared to death by a ' + random.choice(monster) + '\n')
    else:
        print('You have made it through the House! You have been spared!\n')

import random

print('You run into a haunted house and there are 11 doors.\n')

running = True
while running:
    prompt()
    options = input('Pick a door number to walk through: \n')
    make_choice()
    choice = input('Continue? Yes or No? \n')
    if choice == 'No':
        running = False

