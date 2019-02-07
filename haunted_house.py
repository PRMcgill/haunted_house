
print('You have entered into a haunted house. There are 2 doors.')

options = input('Pick a door number to walk through: ')

doors = int(options)
for pathing in options:
    if doors == 2:
        print('Boo! You have been scared to death by a Ghost!')
    else:
        print('You have made it through the House! You have been spared!')


