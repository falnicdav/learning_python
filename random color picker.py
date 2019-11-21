import random
import string


alchohol_markers = ['1', '3', '5', '6', '8', '9', '10', '12', '15', '17', '21', '22', '23', '24', '25', '26', '28', '31', '33', '34', '35', '37', '41', '42', '43', '44', '45', '46',
                     '47', '48', '49', '50', '53', '55', '56', '57', '58', '59', '63', '64', '65', '66', '67', '68', '69', '70', '71', '74', '75', '76', '77', '81', '82', '83', '84', '85',
                    '86', '87', '91', '94', '95', '96', '100', '101', '104', '120', 'BG5', 'BG7', 'BG9', 'CG0.5', 'CG2', 'CG6', 'GG3', 'WG0.5', 'WG1', 'WG4', 'WG5', 'WG8', 'F01', 'F04',
                    'E00 Cotton Pearl', 'R20 Blush', 'E11 Barley Beige', 'E13 Light Suntan', 'E15 Dark Suntan', 'E18 Copper', 'GR4 Evergreen', 'GR3 Grass Green', 'GR2 Dark Sage',
                    'GR1 Green Apple', 'YL2 Summer Sun', 'YO2 Mellow Yellow', 'OR3 Tangerine', 'RD2 Red Coral', 'RD4 Crimson Red', 'BR3 Cinnamon', 'RD3 Vermillion', 'BL6 Royal Blue',
                    'BR1 Taupe', 'BK4 Deep Black']


print('Welcome to random color picker!')


while True:

    for num in range(3):
        color = random.choice(alchohol_markers)
        print('Your random color is: %s' % color)

    response = input('Would you like another set of colors? Type y or n: ')
    if response == 'n':
        break
