from tkinter import Tk, simpledialog, messagebox
import sys

print('Dream World')
root = Tk()
root.withdraw()
answer = {'yes': 'yes'}
description = {'room': {'1': 'You are in a big room. It is furnished with a state of the art spa. There is a large feather on the ground in front of you. Choose a room from 1-5, to look at the feather type 1F',
                        '1a': 'You are in a big room. It is furnished with a state of the art spa.  Choose a room from 1-5.',
                         '2': 'You are in a small room with a really high celing. There is a big window at the top that you can see the sky through. There is no furnature. Chose a room from 1-5',
                         '3': 'You are in a large gym area. There is a pool in fron ot you and work out equipment behind you. Chose a room from 1-5',
                         '4': 'You are in a tall staircase. Looking down, you see a seating area. Above, you see some rundown stores, they are closed.'
                              ' This place seems abandoned. There is a trashcan at the top of the stairs. Chose a room from 1-5, to look in the trashcan type 4T',
                        '4a': 'You are in a tall staircase. Looking down, you see a seating area. Above, you see some rundown stores, they are closed.'
                              ' This place seems abandoned. There is a trashcan at the top of the stairs. Chose a room from 1-5.',
                         '5': 'You are in a park full of beautiful oak trees. Some are saplings as tall as your waist while others are over 1000 feet tall!'
                              ' Somehow, the floor beneath your feet is concrete. There is a piece of paper pinned to a tree in front of you.  Chose a room from 1-5, to look at the paper type 5P.',
                        '4T': 'The trashcan is full of dirt and broken glass but right at the surface you see a bottle of ink. You put it into your inventory. Type 4a to go back.',
                           '5P': 'The piece of paper on the tree in front of you seems to be blank. Type 5 to go back, to open your inventory type I.',
                            '1F': 'The feather in front of you looks to be able to be used to write and upon further inspection you see it is a writing quill. You put it into your inventory. Type 1a to go back.',
                        'I': 'You have a quill and a bottle of ink in your inventory. Type 5 to go back. To combine them type C.',
                        'C': 'You combine the quill and ink. You now have an empty bottle of ink and a quill with ink on it. It should be able to write a something before running out. '
                             ' To go back type 5, to use it type U.',
                        'U': 'What do you want to use the quill on? to choose the paper type P. To choose something else type S, to go back type 5.',
                        'S': 'There is nothing else you can use it on. Type U to go back. Type 5 to return to the room.',
                        'P': 'You choose the paper. What do you want to write? Type random or specific. To return to the room type 5.',
                        'random': 'You write the word watermelon on the paper. It bursts into flames and the world is cast into darkness. Type Z to continue.',
                        'Z': 'You are trapped in darkness for all eternity. GAME OVER. If you wish to restart type 1.',
                        'specific': 'You write the word Home on the page. It bursts into flames and you are blinded by a flash of light. type A to continue.',
                        'A': 'As your vision fades back, you realize your eyes are closed and see that you are in your bedroom. As you sit up in bed, you realize that must have been a dream. type A2 to continue.',
                        'A2': 'Congratulations! You have completed the short interactive fiction story Dream World!. Thank you for playing. To restart, type 1. To end the game type any letter.'}}

inventory = []

room = '1'

introduction = simpledialog.askstring('intro', 'Welcome to Dream World! Do you wish to start the game? type yes or no')
if introduction == 'yes':
    while True:
        room = simpledialog.askstring('room ' + room, description['room'][room])
        if room == '1':
            # do something
            pass
        if room == '2':
            # do something
            pass
else:
    sys.exit()


root.mainloop()
