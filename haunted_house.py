
def prompt():
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

options = input('Pick a door number to walk through: ')

import random

monster = ['Ghoul', 'Ghost', 'Cyclop', 'Zombie']

doors = int(options)
prompt()
    for pathing in options:
        if doors == 2:
         print('Boo! You have been scared to death by a ' + random.choice(monster))
        elif doors == 2:
            print('You have made it through the House! You have been spared!')
        else:
            print('You ran into the wall. Good job. Pick a door')
        break

