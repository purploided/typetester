# i made this for experience lol
# ~nicolas

import time

finished = False

start = time.time() # the start time

tryThis = print('Type: The red green fox ran across a road')
startTyping = input('> ')

if finished == False: # returns the start if finished equals false

    if startTyping == 'The red green fox ran across a road':
        finished = True

if finished == True:
    end = time.time() # the end time
    print(startTyping)
    print('It took you', end - start, 'seconds to type: The red green fox ran across a road')