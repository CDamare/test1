from Tkinter import *
from board_local import *
from time import sleep

print
print
print
print "\t  Welcome to the most amazing game ever created!!!!"
print "\n\t  The rules are fairely simple... Kill all main pieces."
print "\n\t  All players have exactly 10 seconds to take their turns!"
print "\n\t  Once you kill all the pieces on the board that are not pawns,\n\t\t\t\tYOU WIN."
print

sleep(10)
    
window = Tk()
window.wm_geometry("400x400")
window.title("Chess DEATHMATCH")
p = Board(window)    
p.refresh()
window.mainloop()

