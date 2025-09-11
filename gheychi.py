import random

you = input('sang  kaqaz  gheychi : ')
bot = random.randint(0, 2)

if bot == 0:
    bot = 'sang'
elif bot == 1:
    bot = 'kaqaz'
else:
    bot = 'gheychi'


if you == bot :
    print('draw')
elif (you == 'sang' and bot == 'gheychi' )or \
     (you == 'kaqaz' and bot == 'sang') or \
     (you == 'gheychi' and bot == 'kaqaz'):
    print('you win')

elif (bot == 'sang' and you == 'gheychi' )or \
     (bot == 'kaqaz' and you == 'sang') or \
     (bot == 'gheychi' and you == 'kaqaz'):
    print('bot win')
    
else:
    print('enter just sang kaqaz gheychi, try again')