
print('You have entered into a haunted house. There are 11 doors.')

options = int(input('Pick a door number to walk through: '))


for pathing in options:
    if options % 2 == 0:
        print('You have been scared to death by a Ghost!')
    else:
        print('You have made it through the House! You have been spared!')


