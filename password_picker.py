import random
import string


articles = ['a', 'an', 'the']


adjectives = ['loyal', 'loud', 'teeny',
               'cute', 'crazy', 'tired',
               'floofy', 'cloudy', 'sweet',
               'intelligent', 'dangerous', 'fruitful',
               'trustworthy', 'stylish', 'leafy',
              'lovely', 'moony', 'sharp', 'solo', 'artistic']

colors = ['silver', 'turquoise', 'black', 'white', 'green', 'pastel', 'purple',
          'fuschia', 'blue', 'red', 'iridescent', 'pink', 'violet', 'olive']


nouns = ['snake', 'skywing', 'cat',
         'battery', 'cactus', 'leather',
         'book', 'hackysack', 'falcon',
         'charm', 'sky', 'zebra',
         'Nezuko', 'Kagome', 'Ochaco', 'Asuna',
         'Tanjiro', 'Inuyasha', 'Izuku', 'Kirito', 'swordsman', 'sword',
         'rapier']


print('Welcome to Password Picker!')


while True:

    for num in range(3):
        article = random.choice(articles)
        adjective = random.choice(adjectives)
        color = random.choice(colors)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = article + adjective + color + noun + str(number) + special_char
        print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break
