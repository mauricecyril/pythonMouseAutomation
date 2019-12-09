# Python Script to automate mouse scripts

import ctypes
import time

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event?redirectedfrom=MSDN

def move(x,y):
    ctypes.windll.user32.SetCursorPos(x,y)

def singleclick():
    '''Single Left Click'''
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # Left Down MOUSE_LEFTDOWN = 0x0002
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left Up MOUSE_LEFTUP = 0x0004

def doubleclick():
    '''Double Left Click'''
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # Left Down MOUSE_LEFTDOWN = 0x0002
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left Up MOUSE_LEFTUP = 0x0004
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # Left Down MOUSE_LEFTDOWN = 0x0002
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left Up MOUSE_LEFTUP = 0x0004
    
def rightclick():
    '''Single Right Click'''
    ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0) # Right Down MOUSE_RIGHTDOWN = 0x0008
    ctypes.windll.user32.mouse_event(16, 0, 0, 0, 0) # Right Up MOUSE_RIGHTUP = 0x0010
    
def main():
    move(952,179)
    rightclick()
    #time.sleep(15)
    print("Complete")

if __name__ == "__main__":
    main()
