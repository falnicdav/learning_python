import random
import string


adjectives = ['loyal', 'loud', 'teeny',
               'cute', 'crazy', 'tired',
               'floofy', 'cloudy', 'sweet',
               'intelligent', 'dangerous', 'fruitful',
               'turquoise', 'silver', 'leafy']


nouns = ['snake', 'skywing', 'cat',
         'battery', 'cactus', 'leather',
         'book', 'hackysack', 'falcon',
         'charm', 'sky', 'zebra',
         'Nezuko', 'Kagome', 'Ochaco', 'Asuna']


print('Welcome to Password Picker!')


while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
