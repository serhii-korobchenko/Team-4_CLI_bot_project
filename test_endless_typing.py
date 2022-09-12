from pynput import keyboard

command_list = ['hello','add','change', 'phone', 'show', 'good','close', 'exit', 'addnum', 'del',\
         'addbirth', 'nextbirth','see','help','save', 'load','lookup','delrec', 'addemail', 'addnotes',\
           'addadress', 'findtag', 'sortnotes', 
           'sortfiles','guess','checkbirth','changeemail']


def on_press(key):
    try:
        if key == keyboard.Key.esc:
        
        # Stop listener
            return False
        elif key == keyboard.Key.enter:
            print('')
            print(''.join(map(str, main_list)), end='\r', flush=True)

        else:
            main_list.append(key.char)
            for command in command_list:
                #print("command[0]", command[0])
                #print("main_list[0]", main_list[0].char)
                
                if len(main_list) == 1 and command[0] == main_list[0]:
            
                    print(command, end='\t\t\t')

                elif len(main_list) == 2 and command[0] == main_list[0] and command[1] == main_list[1]:

                    print(command, end='\t\t\t')

                elif len(main_list) == 3 and command[0] == main_list[0] and command[1] == main_list[1] and command[2] == main_list[2]:

                    print(command, end='\t\t\t')

            print(''.join(map(str, main_list)), end='\r', flush=True)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

main_list = []

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:   #on_release=on_release
    listener.join()
    

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press)   #on_release=on_release
listener.start()
