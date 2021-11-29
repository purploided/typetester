import time

finished = False

start = time.time()

tryThis = print('Type: The red green fox ran across a road')
startTyping = input('> ')

if finished == False:

    if startTyping == 'The red green fox ran across a road':
        finished = True

if finished == True:
    end = time.time()
    print(startTyping)
    print('It took you', end - start, 'seconds to type: The red green fox ran across a road')