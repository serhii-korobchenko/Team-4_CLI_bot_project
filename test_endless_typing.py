from pynput import keyboard

""" print('Press s or n to continue:')

with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('s'):
        print("YES") """

def on_press(key):
    try:
        print(key.char, end= ' ')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print(' ', end='')
    if key == keyboard.Key.esc:
        # Stop listener
        print(listener.daemon)
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listener.start()