import ctypes
import time

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event?redirectedfrom=MSDN
# https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/
# Bunch of stuff so that the script can send keystrokes to game #

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Direct Input Key Codes  http://www.flint.jp/misc/?q=dik&lang=en
# Create a dictionary with all the key codes
kb = {'Esc' :  0x01, 
        '1' :  0x02, 
        '2' :  0x03, 
        '3' :  0x04, 
        '4' :  0x05, 
        '5' :  0x06, 
        '6' :  0x07, 
        '7' :  0x08, 
        '8' :  0x09, 
        '9' :  0x0A, 
        '0' :  0x0B, 
        '-' :  0x0C, 
        '=' :  0x0D, 
        'Back Space' :  0x0E, 
        'Tab' :  0x0F, 
        'Q' :  0x10, 
        'W' :  0x11, 
        'E' :  0x12, 
        'R' :  0x13, 
        'T' :  0x14, 
        'Y' :  0x15, 
        'U' :  0x16, 
        'I' :  0x17, 
        'O' :  0x18, 
        'P' :  0x19, 
        '[' :  0x1A, 
        ']' :  0x1B, 
        'Enter' :  0x1C, 
        'Ctrl (Left)' :  0x1D, 
        'A' :  0x1E, 
        'S' :  0x1F, 
        'D' :  0x20, 
        'F' :  0x21, 
        'G' :  0x22, 
        'H' :  0x23, 
        'J' :  0x24, 
        'K' :  0x25, 
        'L' :  0x26, 
        ';' :  0x27, 
        '' :  0x28, 
        '`' :  0x29, 
        'Shift (Left)' :  0x2A, 
        '"\"':  0x2B,
        'Z' :  0x2C, 
        'X' :  0x2D, 
        'C' :  0x2E, 
        'V' :  0x2F, 
        'B' :  0x30, 
        'N' :  0x31, 
        'M' :  0x32, 
        '' :  0x33, 
        '.' :  0x34, 
        '/' :  0x35, 
        'Shift (Right)' :  0x36, 
        '* (Numpad)' :  0x37, 
        'Alt (Left)' :  0x38, 
        'Space' :  0x39, 
        'Caps Lock' :  0x3A, 
        'F1' :  0x3B, 
        'F2' :  0x3C, 
        'F3' :  0x3D, 
        'F4' :  0x3E, 
        'F5' :  0x3F, 
        'F6' :  0x40, 
        'F7' :  0x41, 
        'F8' :  0x42, 
        'F9' :  0x43, 
        'F10' :  0x44, 
        'Num Lock' :  0x45, 
        'Scroll Lock' :  0x46, 
        '7 (Numpad)' :  0x47, 
        '8 (Numpad)' :  0x48, 
        '9 (Numpad)' :  0x49, 
        '- (Numpad)' :  0x4A, 
        '4 (Numpad)' :  0x4B, 
        '5 (Numpad)' :  0x4C, 
        '6 (Numpad)' :  0x4D, 
        '+ (Numpad)' :  0x4E, 
        '1 (Numpad)' :  0x4F, 
        '2 (Numpad)' :  0x50, 
        '3 (Numpad)' :  0x51, 
        '0 (Numpad)' :  0x52, 
        '. (Numpad)' :  0x53, 
        'F11' :  0x57, 
        'F12' :  0x58, 
        'F13' :  0x64, 
        'F14' :  0x65, 
        'F15' :  0x66, 
        '=' :  0x8D, 
        '^' :  0x90, 
        '@' :  0x91, 
        ':' :  0x92, 
        '_' :  0x93, 
        'Stop' :  0x95, 
        'Enter (Numpad)' :  0x9C, 
        'Ctrl (Right)' :  0x9D, 
        ', (Numpad)' :  0xB3, 
        '/ (Numpad)' :  0xB5, 
        'Sys Rq' :  0xB7, 
        'Alt (Right)' :  0xB8, 
        'Pause' :  0xC5, 
        'Home' :  0xC7, 
        '↑' :  0xC8, 
        'Page Up' :  0xC9, 
        '←' :  0xCB, 
        '→' :  0xCD, 
        'End' :  0xCF, 
        '↓' :  0xD0, 
        'Page Down' :  0xD1, 
        'Insert' :  0xD2, 
        'Delete' :  0xD3, 
        'Windows' :  0xDB, 
        'Windows' :  0xDC, 
        'Menu' :  0xDD, 
        'Power' :  0xDE, 
        'Windows' :  0xDF}
    

# Keyboard Presses
def keypress(key):
    #time.sleep(.05)
    PressKey(int(kb.get(str(key))))
    #time.sleep(.05)
    ReleaseKey(int(kb.get(str(key))))


# Mouse Move and Click Functions
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
    time.sleep(2)
   
        
    move(98,120) # Move cursor to location
    singleclick()
    time.sleep(1)

    # Input 
    keypress('1')        
    keypress('A')
    keypress('"\"')
    keypress('L')
        
    print("Complete")

if __name__ == "__main__":
    main()




### HEX Codes for Keyboard Presses ###
# 'Esc' = 0x01
# '1' = 0x02
# '2' = 0x03
# '3' = 0x04
# '4' = 0x05
# '5' = 0x06
# '6' = 0x07
# '7' = 0x08
# '8' = 0x09
# '9' = 0x0A
# '0' = 0x0B
# '-' = 0x0C
# '=' = 0x0D
# 'Back Space' = 0x0E
# 'Tab' = 0x0F
# 'Q' = 0x10
# 'W' = 0x11
# 'E' = 0x12
# 'R' = 0x13
# 'T' = 0x14
# 'Y' = 0x15
# 'U' = 0x16
# 'I' = 0x17
# 'O' = 0x18
# 'P' = 0x19
# '[' = 0x1A
# ']' = 0x1B
# 'Enter' = 0x1C
# 'Ctrl (Left)' = 0x1D
# 'A' = 0x1E
# 'S' = 0x1F
# 'D' = 0x20
# 'F' = 0x21
# 'G' = 0x22
# 'H' = 0x23
# 'J' = 0x24
# 'K' = 0x25
# 'L' = 0x26
# ';' = 0x27
# ''' = 0x28
# '`' = 0x29
# 'Shift (Left)' = 0x2A
# '\' = 0x2B
# 'Z' = 0x2C
# 'X' = 0x2D
# 'C' = 0x2E
# 'V' = 0x2F
# 'B' = 0x30
# 'N' = 0x31
# 'M' = 0x32
# ',' = 0x33
# '.' = 0x34
# '/' = 0x35
# 'Shift (Right)' = 0x36
# '* (Numpad)' = 0x37
# 'Alt (Left)' = 0x38
# 'Space' = 0x39
# 'Caps Lock' = 0x3A
# 'F1' = 0x3B
# 'F2' = 0x3C
# 'F3' = 0x3D
# 'F4' = 0x3E
# 'F5' = 0x3F
# 'F6' = 0x40
# 'F7' = 0x41
# 'F8' = 0x42
# 'F9' = 0x43
# 'F10' = 0x44
# 'Num Lock' = 0x45
# 'Scroll Lock' = 0x46
# '7 (Numpad)' = 0x47
# '8 (Numpad)' = 0x48
# '9 (Numpad)' = 0x49
# '- (Numpad)' = 0x4A
# '4 (Numpad)' = 0x4B
# '5 (Numpad)' = 0x4C
# '6 (Numpad)' = 0x4D
# '+ (Numpad)' = 0x4E
# '1 (Numpad)' = 0x4F
# '2 (Numpad)' = 0x50
# '3 (Numpad)' = 0x51
# '0 (Numpad)' = 0x52
# '. (Numpad)' = 0x53
# 'F11' = 0x57
# 'F12' = 0x58
# 'F13' = 0x64
# 'F14' = 0x65
# 'F15' = 0x66
# 'Enter (Numpad)' = 0x9C
# 'Ctrl (Right)' = 0x9D
# ', (Numpad)' = 0xB3
# '/ (Numpad)' = 0xB5
# 'Sys Rq' = 0xB7
# 'Alt (Right)' = 0xB8
# 'Pause' = 0xC5
# 'Home' = 0xC7
# '↑' = 0xC8
# 'Page Up' = 0xC9
# '←' = 0xCB
# '→' = 0xCD
# 'End' = 0xCF
# '↓' = 0xD0
# 'Page Down' = 0xD1
# 'Insert' = 0xD2
# 'Delete' = 0xD3
# 'Windows' = 0xDB
# 'Windows' = 0xDC
# 'Menu' = 0xDD
# 'Power' = 0xDE
# 'Windows' = 0xDF
# 'Kana' = 0x70
# 'Convert' = 0x79
# 'No Convert' = 0x7B
# '¥' = 0x7D
# '=' = 0x8D
# '^' = 0x90
# '@' = 0x91
# ':' = 0x92
# '_' = 0x93
# 'Kanji' = 0x94
# 'Stop' = 0x95
# '(Japan AX)' = 0x96
# '(J3100)' = 0x97
