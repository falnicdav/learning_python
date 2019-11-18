from tkinter import Tk, simpledialog, messagebox
import sys

print('Dream World')
root = Tk()
root.withdraw()
answer = {'yes': 'yes'}
description = {'1': 'You are in a big room. It is furnished with a state of the art spa.',
               '2': 'You are in a small room with a really high celing. There is a big window at the top that you can see the sky through. There is no furnature. Chose a room from 1-5',
               '3': 'You are in a large gym area. There is a pool in fron ot you and work out equipment behind you. Chose a room from 1-5',
               '4': 'You are in a tall staircase. Looking down, you see a seating area. Above, you see some rundown stores, they are closed.'
                    ' This place seems abandoned. Chose a room from 1-5.',
                    '5': 'You are in a park full of beautiful oak trees. Some are saplings as tall as your waist while others are over 1000 feet tall!'
                              ' Somehow, the floor beneath your feet is concrete. Chose a room from 1-5.'}

room = '1'

introduction = simpledialog.askstring('intro', 'Welcome to Dream World! Do you wish to start the game? type yes or no')
if introduction == 'yes':
    while True:
        room = simpledialog.askstring('room ' + room, description['room'])

root.mainloop()
