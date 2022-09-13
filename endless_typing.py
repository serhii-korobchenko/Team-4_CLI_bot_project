from pynput import keyboard

command_list = ['hello','add','change', 'phone', 'show', 'good','close', 'exit', 'addnum', 'del',\
         'addbirth', 'nextbirth','see','help','save', 'load','lookup','delrec', 'addemail', 'addnotes',\
           'addadress', 'findtag', 'sortnotes', 
           'sortfiles','guess','checkbirth','changeemail']


def on_press(key):
    
    
    global main_list_guess
    global join_command_list
    
    try:
        if key == keyboard.Key.esc:
        
        # Stop listener
            return False

        elif key == keyboard.Key.enter:
            #print('')
            #print(''.join(map(str, main_list_guess)), end='\r', flush=True)
            return False

            

        elif key == keyboard.Key.shift:
            pass

        elif key == keyboard.Key.space:
            main_list_guess.append(' ')

        elif key == keyboard.Key.backspace:

            if len(main_list_guess) >= 0:
                main_list_guess.pop()
                print('                                                                                     ', end='\r')
                print(''.join(map(str, main_list_guess)), end='\r', flush=True)

        else:
            main_list_guess.append(key.char)
            for command in command_list:
                                              
                if len(main_list_guess) == 1 and command[0] == main_list_guess[0]:
            
                    join_command_list.append(command)

                elif len(main_list_guess) == 2 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1]:

                    join_command_list.append(command)

                elif len(main_list_guess) == 3 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1] and command[2] == main_list_guess[2]:

                    join_command_list.append(command)

                elif len(main_list_guess) == 4 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1] and command[2] == main_list_guess[2] and command[3] == main_list_guess[3]:

                    join_command_list.append(command)

            print('                                                                                    ', end='\r')
            print(''.join(map(str, main_list_guess)), end='\r\t\t\t\t', flush=True)
            print(', '.join(map(str, join_command_list)), end='\r', flush=True)
            join_command_list.clear()

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

    except IndexError:
        print('', end='')

def main_guess(command_list):
    
    global main_list_guess
    global join_command_list
   
    main_list_guess = []
    join_command_list = []


    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:   #on_release=on_release
        listener.join()
        
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press)   #on_release=on_release
    listener.start()
    listener.stop()

    return ''.join(map(str, main_list_guess))

if __name__ == '__main__':
    
    result = main_guess(command_list)
    print ('RETURN :', result)
    
