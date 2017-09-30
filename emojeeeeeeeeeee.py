import random

i = 0
sum = ''
while i < 101:
    i = i + 1
    base = '\U0001f'
    rand = str(random.randint(600,630))
    emoji = base + rand
    emoji_u  = emoji.decode('unicode-escape')
    print emoji_u
#    sum += emoji
#print sum
#emoji_u  = sum.decode('unicode-escape')



