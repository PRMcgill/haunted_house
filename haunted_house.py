
print('You run into a haunted house and there are 11 doors. \n'
        'What door do you choose? \n'
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



import random

monster = ['Ghoul', 'Ghost', 'Cyclop', 'Zombie']
options = input('Pick a door number to walk through: ')
doors = int(options)

if doors > 11 or doors < 1:
    print('You ran into the wall. Good job. Pick a door.')
    if doors % 2 == 0:
        print('Boo! You have been scared to death by a ' + random.choice(monster))
    else doors == 2:
        print('You have made it through the House! You have been spared!')

