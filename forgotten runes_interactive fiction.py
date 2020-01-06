#from tkinter import Tk, simpledialog, messagebox
import tkinter as tk
import tkinter.simpledialog as simpledialog
import sys
import textwrap


def get_item(item, room, next_room):
    global inventory
    global room_inventory

    print(item, room, next_room)
    print(room_inventory[room])
    if item in room_inventory[room]:
        #messagebox.showinfo("message", "You put the " + item + " in your inventory.")
        message = "You put the " + item + " in your inventory.\n"
        T.insert(tk.END, message)
        T.see("end")
        print(inventory)
        print(room_inventory[room])
        inventory.append(item)
        room_inventory[room].remove(item)
        print(inventory)
        print(room_inventory[room])
        return next_room
    else:
        #messagebox.showinfo("message", "The " + item + " has already been taken.")
        message = "The " + item + " has already been taken.\n"
        T.insert(tk.END, message)
        T.see("end")
        return next_room


def drop_item(item, room, next_room):
    global inventory
    global room_inventory
    global T

    print(item, room, next_room)
    print(inventory)
    print(room_inventory[room])
    if item in inventory:
        #messagebox.showinfo("message", "You put the " + item + " in room " + room +".")
        message = "You put the " + item + " in room " + room +".\n"
        T.insert(tk.END, message)
        T.see("end")
        print(inventory)
        print(room_inventory[room])
        room_inventory[room].append(item)
        inventory.remove(item)
        print(inventory)
        print(room_inventory[room])
        return next_room
    else:
        #messagebox.showinfo("message", "You are not holding the " + item + ".")
        message = "You are not holding the " + item + ".\n"
        T.insert(tk.END, message)
        T.see("end")
        return next_room

def examine_item(item, room, next_room):
    global inventory
    global room_inventory
    global T

    print(item)
    if item in inventory:
        message = 'You examine the ' + item + '.\n'
        T.insert(tk.END, message)
        T.see("end")
       # print(description[item])
        display_room('item', object)
        return next_room

def show_help():
    message = 'Your valid commands are: \n'
    for command in valid_commands:
        message= message + command+ '\n'
    T.insert(tk.END, message)
    T.see("end")


def do_command():
    global T

    cmdtext = cmd.get()
    addtext = "\n"+cmd.get() + "\n"
    T.insert(tk.END, addtext)
    T.see("end")
    cmd.delete(0, tk.END)
    do_room(cmdtext)


answer = {'yes': 'yes'}
description = {'room': {'1': 'You are in a big room. It is furnished with a state of the art spa. \n'
                             'Choose a room from 1-5, to look at the feather type 1F.',
                         '2': 'You are in a small room with a really high ceiling. There is a big window at the top that you can see the sky through. \n'
                              'There is no furniture. Chose a room from 1-5',
                         '3': 'You are in a large gym area. There is a pool in front of you and work out equipment behind you. \n'
                              'Chose a room from 1-5',
                        '4': 'You are in a tall staircase. Looking down, you see a seating area.\n'
                              ' Above, you see some rundown stores, they are closed.\n'
                              ' This place seems abandoned. There is a trashcan at the top of the stairs.\n'
                              ' Choose a room: 1a, 2, 3, 4a and 5.',
                         '5': 'You are in a park full of beautiful oak trees. Some are saplings as tall as your waist while others are over 1000 feet tall!\n'
                              ' Somehow, the floor beneath your feet is concrete. There is a piece of paper pinned to a tree in front of you.  \n'
                              'Chose a room from 1-5, to look at the paper type 5P. You can open your inventory here, type "I" to do so.',
                        'i': '',
                        'c': 'You combine the quill and ink. You now have an empty bottle of ink and a quill with ink on it. \n'
                             'It should be able to write a something before running out. '
                             ' To go back type 5, to use it type U.',
                        'u': 'What do you want to use the quill on? to choose the paper type P.\n'
                             ' To choose something else type S, to go back type 5.',
                        's': 'There is nothing else you can use it on.\n'
                             ' Type U to go back. Type 5 to return to the room.',
                        'p': 'You choose the paper. What do you want to write? \n'
                             'Type "random" or "specific". To return to the room type 5.',
                        'random': 'You write the word watermelon on the paper. \n'
                                  'It bursts into flames and the world is cast into darkness. Type Z to continue.',
                        'z': 'You are trapped in darkness for all eternity. GAME OVER. To exit type quit.',
                        'specific': 'You write the word Home on the page.\n'
                                    ' It bursts into flames and you are blinded by a flash of light. type A to continue.',
                        'a': 'As your vision fades back, you realize your eyes are closed and see that you are in your bedroom.\n'
                             ' You open them and as you sit up in bed, you realize that must have been a dream. type A2 to continue. \n'
                             'Congratulations! You have completed the short interactive fiction story Dream World!. Thank you for playing. To exit type quit.',
                        'quit': 'you quit',
                        'trashcan': 'The trashcan is full of dirt and broken glass.',
                        #'help': 'Your valid commands are: go, take, get, drop, use, combine, examine, inventory, i, open, look and wait.'
                        },
               'item': {
                   'bottle': 'A small clear bottle with a little bit of ink in it. There is a black lid stopping the ink from coming out.\n'
                                    ' There is just enough ink inside to write a word or two.',
                   'feather':'A large tawny colored wing feather. The tip of the feather is cut in a way that makes it seem to be a writing quill.',
                   'paper':'A blank piece of parchment. It has a piece ripped off of the bottom, I wonder what could have happened to it?',
                    'trashcan': 'The trashcan is full of dirt and broken glass.'}
               }

inventory = []
room_inventory = {}
for r in description['room'].keys():
    room_inventory[r] = []
room_inventory['1'].append('feather')
room_inventory['trashcan'].append('bottle')
print(room_inventory)
print(inventory)
points = 0
room = '1'
previous_room = '1'
turn = 0
valid_commands = ['go', 'take', 'get', 'drop', 'use', 'combine', 'examine', 'inventory', 'i', 'open', 'look', 'l', 'wait']

def do_intro():
    global T
    
    #displaytext = 'Welcome to Dream World! Do you wish to start the game? type yes or no'
    displaytext = 'Welcome to Dream World!\n\n'
    T.insert(tk.END, displaytext)
    T.see("end")
    display_room('room', room)

def display_room(object_type, object):
    global T

    if object_type == 'item':
        room_description = textwrap.fill(description['item'][object], 75) + '\n'
    elif object_type == 'room':
        room_description = textwrap.fill(description['room'][object], 75) + '\n'
    else:
        room_description = 'You are trying to examine something that doesn\'t exist.'
    if len(room_inventory[room])>0:
        room_description += 'in the room you see: \n'
        for item in room_inventory[room]:
            room_description += '  ' + item + '\n'
    T.insert(tk.END, room_description)
    T.see("end")

def show_inventory():
    message = 'You are holding: \n'
    for item in inventory:
        message = message + item + '\n'
    # messagebox.showinfo("Inventory", message)
    if ('feather' in inventory) and ('bottle' in inventory):
        message = message + '\n' + 'To combine them type "C".'
    T.insert(tk.END, message)
    T.see("end")

def show_text(message):
    global T

    message = textwrap.fill(message, 75) + '\n'
    T.insert(tk.END, message)
    T.see("end")

def do_room(cmdtext):
#introduction = simpledialog.askstring('intro', 'Welcome to Dream World! Do you wish to start the game? type yes or no')
#if introduction == 'yes':
#    while True:
    global previous_room
    global room
    global turn
    global points
    global T
    
    previous_room = room
    turn = turn + 1

    #room = simpledialog.askstring(
    #    'room ' + room + ', points: ' + str(points) +', turn: ' + str(turn) + ', Type quit to exit',
    #    room_description)

    cmdtext = cmdtext.lower()

    if len(cmdtext.split(" ")) == 2:
        (command, object) = cmdtext.split(" ")
        if command in valid_commands:
            message = 'You type the command:' + command
            show_text(message)
            message = 'The object you chose was:' + object
            show_text(message)
            if command == 'go':
                room = object
                if room in description['room'].keys():
                    display_room('room', room)
                else:
                    message = 'Invalid room.'
                    show_text(message)
            elif command in ['take', 'get']:
               # message = 'You attempt to take the: ' + object
                #show_text(message)
                room = get_item(object, room, room)
            elif command == 'drop':
                drop_item(object, room, room)
            elif command == 'examine':
                item = object
                if item in description['item'].keys():
                    display_room('item', item)
                else:
                    message = 'Invalid item.'
                    show_text(message)

    elif len(cmdtext.split(" ")) == 1:
        print(cmdtext)
        if cmdtext in ['i', 'inventory']:
            object = cmdtext
            show_inventory()
        elif cmdtext == 'help':
            object = cmdtext
            show_help()
        elif cmdtext in ['l', 'look']:
            object = cmdtext
            display_room('room', room)
    else:
        message = 'Invalid command'
        show_text(message)

    room = object
    if room in description['room'].keys():
        pass
    else:
        #messagebox.showinfo("error", " You must enter a valid room, try again. \n"
        #                             "You can type quit to exit the game.")
        message = " You must enter a valid room, try again. \nYou can type quit to exit the game.\n"
       # T.insert(tk.END, message)
       # T.see("end")
        room = previous_room
    if room == 'quit':
        #sys.exit()
        close_window()
    if room == '1f':
        points += + 3
    if room == '4t':
        points +=  3
    if room == 'c':
        points += + 2
    if room == 'u':
        points += + 2
    if room == 'p':
        points += + 2
    if room == 'z':
        points += - 3
    if room == 'specific':
        points += + 1
    if room == 'a':
        points += + 1
    if room == 'a2':
        points += + 3
    if room == 'take feather':
        #room = get_item('feather', '1', '1a')
        pass
    if room == 'take ink':
        #room = get_item('bottle of ink', '4T','4')
        pass
    if room == 'drop feather':
        #room = drop_item('feather', '1', '1')
        pass
    if room == 'drop ink':
        #room = drop_item('bottle of ink', '4T', '4T')
        pass
    if room == 'i':
        message = 'You are holding: \n'
        for item in inventory:
            message = message + item + '\n'
        #messagebox.showinfo("Inventory", message)
        if ('feather' in inventory) and ('bottle' in inventory):
            message = message + '\n' + 'To combine them type "C".'
        #T.insert(tk.END, message)
        #T.see("end")
        #messagebox.showinfo("Inventory", message)
        room = previous_room
    if room == '1':
        # do something
        pass
    if room == '2':
        # do something
        pass
    
    #display_room(room)
#else:
#    sys.exit()

def close_window ():
    root.destroy()


print('Dream World')
root = tk.Tk()
#root.withdraw()
S = tk.Scrollbar(root)
T = tk.Text(root, height=25, width=80)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
L = tk.Label(root, text="Command: ")
L.pack()
cmd = tk.Entry(root)
cmd.pack()
S = tk.Button(root, text="Submit", command=do_command)
S.pack()
Q = tk.Button(root, text="Quit", command=close_window)
Q.pack()

do_intro()

root.mainloop()
tk.mainloop()
