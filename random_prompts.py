import random
import string


articles = ['some ', 'one ', 'that ', 'a ton of ', 'barely ', 'this ', 'these ', 'the ', 'a ton of the ']


adjectives = ['loyal ', 'loud ', 'teeny ', 'adventurous ', 'aggressive ', 'agreeable ', 'alert ', 'alive ', 'amused ', 'angry ', 'annoyed ', 'annoying ', 'anxious ', 'arrogant ', 'ashamed '
               'cute ', 'crazy ', 'tired ', 'attractive ', 'average ', 'awful', 'bad ', 'beautiful ', 'better ', 'bewildered ', 'bloody ', 'blue-eyed ', 'blushing ', 'bored ', 'brainy ',
               'floofy ', 'cloudy ', 'sweet ', 'brave ', 'breakable ', 'bright ', 'busy ', 'calm ', 'careful ', 'cautious ', 'charming ', 'cheerful ', 'clean ', 'clever ', 'clumsy ', 'colorful ',
               'intelligent ', 'dangerous ', 'fruitful ', 'combative ', 'comfortable ', 'concerned ', 'condemned ', 'confused ', 'cooperative ', 'courageous ', 'creepy', 'crowded ', 'cruel ',
               'trustworthy ', 'stylish ', 'leafy ', 'curious ', 'dangerous ', 'dark ', 'dead ', 'defeated ', 'defiant ', 'delightful ', 'depressed ', 'determined ', 'different ', 'difficult ', 
              'lovely ', 'moony ', 'sharp ', 'solo ', 'artistic ', 'adorable ', 'disgusted ', 'distinct ', 'disturbed ', 'dizzy ', 'doubtful ', 'drab ', 'dull ', 'eager ', 'easy ', 'elated '
              'elegant ', 'embarrased ', 'enchanting ', 'encouraging ', 'energetic ', 'enthusiastic ', 'envious ', 'evil ', 'excited ', 'expensive ', 'exuberant ', 'fair ', 'faithful ',
              'famous ', 'fancy ', 'fantastic ', 'fierce ', 'filthy ', 'fine ', 'foolish ', 'fragile ', 'frail ', 'frantic ', 'friendly ', 'frightened ', 'funny ', 'gentle ',
              'gifted ', 'glamorous ', 'gleaming ', 'glorious ', 'good ', 'gorgeous ', 'graceful ', 'grieving ', 'grotesque ', 'grumpy ', 'handsome ', 'happy ', 'healthy ', 'helpful ',
              'helpless ', 'hilarious ', 'homeless ', 'homely ', 'horrible ', 'hungry ', 'hurt ', 'ill ', 'important ', 'impossible ', 'innocent ', 'inquisitive ', 'itchy ', 'jealous ',
              'jittery ', 'jolly ', 'joyous ', 'kind ', 'lazy ', 'light ', 'lively ', 'lonely ', 'long ', 'lovely ', 'lucky ', 'maginicent ', 'misty ', 'modern ', 'motionless', 'muddy ',
              'mushy ', 'mysterious ', 'nasty ', 'naughty ', 'nervous ', 'nice ', 'nutty ', 'obedient ', 'obnoxious ', 'odd ', 'old-fashioned ', 'open ', 'outrageous ', 'outstanding ',
              'panicky ', 'perfect ', 'plain ', 'pleasant ', 'poised ', 'poor ', 'powerful ', 'precious ', 'prickly ', 'proud ', 'putrid ', 'puzzled ', 'quaint ', 'real ', 'relieved ', 'repulsive ',
              'rich ', 'scary', 'spooky ', 'selfish ', 'shiny ', 'shy ', 'silly ', 'sleepy ', 'smiling ', 'smoggy ', 'sore ', 'sparkling ', 'splendid ', 'spotless ', 'stormy ', 'strange ', 'stupid ',
              'successful ', 'super ', 'talented ', 'tame ', 'tender ', 'tense ', 'terrible ', 'tasty ', 'thankful ', 'thoughtful ', 'thoughtless ', 'tired ', 'tough ', 'troubled ', 'ugliest',
              'ugly ', 'uninterested ', 'unsightly ', 'unusual ', 'upset ', 'uptight ', 'vast ', 'victorious ', 'vivacious ', 'wandering ', 'weary ', 'wicked ', 'wide-eyed ', 'wild ', 'witty ',
              'worrisome ', 'worried ', 'wrong ', 'zany ', 'zealous ']

colors = ['crimson ', 'red ', 'coral ', 'hot pink ', 'pink ', 'light pink ', 'orangered ', 'burnt orange ', 'orange ', 'yellow-orange ', 'yellow ', 'olive ', 'green ', 'forest green ',
          'mint ', 'aquamarine ', 'blue ', 'royal blue ', 'navy ', 'lavender ', 'violet ', 'purple ', 'fuchsia ', 'white ', 'light grey ', 'dark grey ', 'black ', 'silver ', 'bronze ',
          'gold ', 'rust ', 'pastel ', 'neon ', 'tan ', 'brown ', 'chocolate ', 'clear ', 'frosted ']


nouns = ['aardvark', 'abbey', 'abbot', 'abductee', 'abductor', 'ability', 'abomination', 'absence', 'abstract', 'abyss', 'academia', 'academy', 'accident', 'accomplishment', 'adult',
         'aeroplane', 'air', 'aircraft Carrier', 'Airforce', 'Airport', 'Album', 'Alphabet', 'Apple', 'Arm', 'Army', 'Baby', 'Backpack', 'Balloon', 'Banana', 'Bank', 'Barbecue',
         'Bathroom', 'Bathtub', 'Bed', 'Bee', 'Bible', 'bribe', 'Bird', 'Bomb', 'Book', 'Boss', 'Bottle', 'Bowl', 'Box', 'Boy', 'Brain', 'Bridge', 'Butterfly', 'Button', 'Cappuccino',
         'Car', 'Car-race', 'Carpet', 'Carrot', 'Cave', 'cloud', 'Chair', 'Chess Board', 'Chief', 'Child', 'Chisel', 'Chocolates', 'Church', 'Circle', 'Circus', 'Clock', 'Clown', 'Coffee',
         'Coffee-shop', 'Comet', 'Compact Disc', 'Compass', 'Computer', 'Crystal', 'Cup', 'Cycle', 'Data Base', 'dagger', 'Desk', 'Diamond', 'Dress', 'Drill', 'deity', 'Drink', 'Drum', 'Dung', 'Ears',
         'Earth', 'Egg', 'Electricity', 'Elephant', 'Eraser', 'Explosive', 'Eyes', 'Family', 'Fan', 'falcon', 'Feather', 'Festival', 'Film', 'Finger', 'Fire', 'Floodlight', 'Flower',
         'Foot', 'Fork', 'Freeway', 'Fruit', 'Fungus', 'Game', 'gun', 'Garden', 'Gas', 'Gate', 'Gemstone', 'Girl', 'Gloves', 'God', 'Grapes', 'godess', 'Guitar', 'Hammer', 'Hat', 'Hieroglyph',
         'Highway', 'Horoscope', 'Horse', 'Hose', 'Ice', 'Ice-cream', 'Insect', 'Jet fighter', 'Junk', 'Kaleidoscope', 'Kitchen', 'Knife', 'Leather jacket', 'Leg', 'Library', 'Liquid',
         'Magnet', 'Man', 'Map', 'Maze', 'Meat', 'Meteor', 'Microscope', 'Milk', 'Milkshake', 'Mist', 'Money $$$$', 'Monster', 'Mosquito', 'Mouth', 'Nail', 'Navy', 'Necklace', 'Needle',
         'Onion', 'PaintBrush', 'Pants', 'Parachute', 'Passport', 'Pebble', 'Pendulum', 'Pepper', 'Perfume', 'Pillow', 'Plane', 'Planet', 'pocket', 'Post-office', 'Potato', 'Printer',
         'Prison', 'Pyramid', 'Radar', 'Rainbow', 'Record', 'Restaurant', 'Rifle', 'Ring', 'Robot', 'Rock', 'Rocket', 'Roof', 'Room', 'Rope', 'Saddle', 'Salt', 'Sandpaper', 'Sandwich',
         'Satellite', 'School', 'Ship', 'shoes', 'Shop', 'Shower', 'Signature', 'Skeleton', 'skull', 'Slave', 'Snail', 'software', 'solid', 'Space Shuttle', 'spectre', 'Spectrum',
         'Sphere', 'Spice', 'Spiral', 'Spoon', 'Sports-car', 'Spot Light', 'Square', 'shape', 'Staircase', 'Star', 'Stomach', 'Sun', 'Sunglasses', 'Surveyor', 'Swimming Pool', 'Sword',
         'Table', 'Tapestry', 'Teeth', 'Telescope', 'Television', 'Tennis racquet', 'Thermometer', 'Tiger', 'Toilet',
         'Tongue', 'Torch', 'Torpedo', 'Train', 'Treadmill', 'Triangle', 'Tunnel', 'Typewriter', 'Umbrella', 'Vacuum', 'Vampire', 'Videotape',
         'Vulture', 'Water', 'Weapon', 'Web', 'Wheelchair', 'Window', 'Woman', 'Worm', 'X-ray']
 

print('Welcome to Random Prompts!')


while True:

    for num in range(3):
        article = random.choice(articles)
        adjective = random.choice(adjectives)
        color = random.choice(colors)
        noun = random.choice(nouns)

        prompt = article + adjective + color + noun 
        print('Your new prompt is: %s' % prompt)

    response = input('Would you like another prompt? Type y or n: ')
    if response == 'n':
        break
