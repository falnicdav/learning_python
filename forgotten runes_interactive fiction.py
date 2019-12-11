from tkinter import Tk, simpledialog, messagebox
import sys


def get_item(item, room, next_room):
    global inventory
    global room_inventory

    print(item, room, next_room)
    print(room_inventory[room])
    if item in room_inventory[room]:
        messagebox.showinfo("message", "You put the " + item + " in your inventory.")
        print(inventory)
        print(room_inventory[room])
        inventory.append(item)
        room_inventory[room].remove(item)
        print(inventory)
        print(room_inventory[room])
        return next_room
    else:
        messagebox.showinfo("message", "The " + item + " has already been taken.")
        return next_room


print('Dream World')
root = Tk()
root.withdraw()
answer = {'yes': 'yes'}
description = {'room': {'1': 'You are in a big room. It is furnished with a state of the art spa. \n'
                             'Choose a room from 1-5, to look at the feather type 1F',
                        '1a': 'You are in a big room. It is furnished with a state of the art spa.  \n'
                              'Choose a room from 1a-5.',
                         '2': 'You are in a small room with a really high ceiling. There is a big window at the top that you can see the sky through. \n'
                              'There is no furniture. Chose a room from 1-5',
                         '3': 'You are in a large gym area. There is a pool in front of you and work out equipment behind you. \n'
                              'Chose a room from 1-5',
                         '4': 'You are in a tall staircase. Looking down, you see a seating area. \n'
                              'Above, you see some rundown stores, they are closed. \n'
                              ' This place seems abandoned. There is a trashcan at the top of the stairs. \n'
                              'Chose a room from 1-5, to look in the trashcan type 4T',
                        '4a': 'You are in a tall staircase. Looking down, you see a seating area.\n'
                              ' Above, you see some rundown stores, they are closed.\n'
                              ' This place seems abandoned. There is a trashcan at the top of the stairs.\n'
                              ' Choose a room: 1a, 2, 3, 4a and 5.',
                         '5': 'You are in a park full of beautiful oak trees. Some are saplings as tall as your waist while others are over 1000 feet tall!\n'
                              ' Somehow, the floor beneath your feet is concrete. There is a piece of paper pinned to a tree in front of you.  \n'
                              'Chose a room from 1-5, to look at the paper type 5P.',
                        '4T': 'The trashcan is full of dirt and broken glass. \n'
                              'Type 4a to go back, or to put the bottle of ink in your inventory type "take ink".',
                           '5P': 'The piece of paper on the tree in front of you seems to be blank. \n'
                                 'Type 5 to go back, to open your inventory type I.',
                            '1F': 'The feather in front of you looks to be able to be used to write and upon further inspection you see it is a writing quill. \n'
                                  'You can type 1 to go back, or to take it type "take feather".',
                        'I': '',
                        'C': 'You combine the quill and ink. You now have an empty bottle of ink and a quill with ink on it. \n'
                             'It should be able to write a something before running out. '
                             ' To go back type 5, to use it type U.',
                        'U': 'What do you want to use the quill on? to choose the paper type P.\n'
                             ' To choose something else type S, to go back type 5.',
                        'S': 'There is nothing else you can use it on.\n'
                             ' Type U to go back. Type 5 to return to the room.',
                        'P': 'You choose the paper. What do you want to write? \n'
                             'Type "random" or "specific". To return to the room type 5.',
                        'random': 'You write the word watermelon on the paper. \n'
                                  'It bursts into flames and the world is cast into darkness. Type Z to continue.',
                        'Z': 'You are trapped in darkness for all eternity. GAME OVER. To exit type quit.',
                        'specific': 'You write the word Home on the page.\n'
                                    ' It bursts into flames and you are blinded by a flash of light. type A to continue.',
                        'A': 'As your vision fades back, you realize your eyes are closed and see that you are in your bedroom.\n'
                             ' You open them and as you sit up in bed, you realize that must have been a dream. type A2 to continue.',
                        'A2': 'Congratulations! You have completed the short interactive fiction story Dream World!. Thank you for playing. To exit type quit.',
                        'quit': 'you quit',
                        'take feather':'',
                        'take ink':''},
               'item': {
                   'bottle of ink': 'A small clear bottle with a little bit of ink in it. There is a black lid stopping the ink from coming out.\n'
                                    ' There is just enough ink inside to write a word or two.',
                   'feather':'A large tawny colored wing feather. The tip of the feather is cut in a way that makes it seem to be a writing quill.',
                   'paper':'A blank piece of parchment. It has a piece ripped off of the bottom, I wonder what could have happened to it?'}
               }

inventory = []
room_inventory = {}
for r in description['room'].keys():
    room_inventory[r] = []
room_inventory['1'].append('feather')
room_inventory['4T'].append('bottle of ink')
print(room_inventory)
print(inventory)
point = 0
room = '1'
previous_room = '1'
turn = 0


introduction = simpledialog.askstring('intro', 'Welcome to Dream World! Do you wish to start the game? type yes or no')
if introduction == 'yes':
    while True:
        previous_room = room
        points = point
        turn = turn + 1
        room_description = description['room'][room]  + '\n'
        if len(room_inventory[room])>0:
            room_description += 'in the room you see: \n'
            for item in room_inventory[room]:
                room_description += '  ' + item + '\n'
        room = simpledialog.askstring('room ' + room + ', points: ' + str(points) +', turn: ' + str(turn) + ', Type quit to exit', room_description)
        if room in description['room'].keys():
            pass
        else:
            messagebox.showinfo("error", " You must enter a valid room, try again. \n"
                                         "You can type quit to exit the game.")
            room = previous_room
        if room == 'quit':
            sys.exit()
        if room == '1F':
            point = point + 3
        if room == '4T':
            point = points + 3
        if room == 'C':
            point = point + 2
        if room == 'U':
            point = point + 2
        if room == 'P':
            point = point + 2
        if room == 'Z':
            point = point - 3
        if room == 'specific':
            point = point + 1
        if room == 'A':
            point = point + 1
        if room == 'A2':
            point = point + 3
        if room == 'take feather':
            room = get_item('feather', '1', '1a')
        if room == 'take ink':
            room = get_item('bottle of ink', '4T','4a')
        if room == 'I':
            message = 'You are holding: \n'
            for item in inventory:
                message = message + item + '\n'
            messagebox.showinfo("Inventory", message)
            room = previous_room
        if room == '1':
            # do something
            pass
        if room == '2':
            # do something
            pass
else:
    sys.exit()


root.mainloop()
