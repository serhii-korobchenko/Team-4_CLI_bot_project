from pynput import keyboard

command_list = ['hello','add','change', 'phone', 'show', 'good','close', 'exit', 'addnum', 'del',\
         'addbirth', 'nextbirth','see','help','save', 'load','lookup','delrec', 'addemail', 'addnotes',\
           'addadress', 'findtag', 'sortnotes', 
           'sortfiles','guess','checkbirth','changeemail']


main_list = []
join_command_list = []

def on_press(key):
    try:
        if key == keyboard.Key.esc:
        
        # Stop listener
            return False
        elif key == keyboard.Key.enter:
            print('')
            print(''.join(map(str, main_list)), end='\r', flush=True)
            return False

        elif key == keyboard.Key.shift:
            pass

        elif key == keyboard.Key.space:
            main_list.append(' ')

        elif key == keyboard.Key.backspace:

            if len(main_list) >= 0:
                main_list.pop()
                print('                                                                                                            ', end='\r')
                print(''.join(map(str, main_list)), end='\r', flush=True)

        else:
            main_list.append(key.char)
            for command in command_list:
                              
                
                if len(main_list) == 1 and command[0] == main_list[0]:
            
                    join_command_list.append(command)

                elif len(main_list) == 2 and command[0] == main_list[0] and command[1] == main_list[1]:

                    join_command_list.append(command)

                elif len(main_list) == 3 and command[0] == main_list[0] and command[1] == main_list[1] and command[2] == main_list[2]:

                    join_command_list.append(command)

                elif len(main_list) == 4 and command[0] == main_list[0] and command[1] == main_list[1] and command[2] == main_list[2] and command[3] == main_list[3]:

                    join_command_list.append(command)

            print('                                                                                                            ', end='\r')
            print(''.join(map(str, main_list)), end='\r\t\t\t\t', flush=True)
            print(', '.join(map(str, join_command_list)), end='\r', flush=True)
            join_command_list.clear()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

    except IndexError:
        print('', end='')

def main_guess():


    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:   #on_release=on_release
        listener.join()
        
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press)   #on_release=on_release
    listener.start()

if __name__ == '__main__':
    
    main_guess()
