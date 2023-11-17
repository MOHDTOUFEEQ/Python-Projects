import curses
from curses import wrapper
import time
import random
import mysql.connector
f1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*******',
    database='*******'
)
cursor = f1.cursor()
def welcome(stdscr):
    name = ""
    stdscr.clear()
    stdscr.addstr("WELCOME TO TYPING TEST \n", curses.color_pair(1))
    stdscr.addstr("PRESS ANY KEY TO CONTINUE", 2)
    stdscr.refresh()
    stdscr.getkey()
    stdscr.clear()
    stdscr.addstr("Enter your name:", curses.color_pair(1))
    while True:
        key = stdscr.getkey()
        if key == '\n':
            break
        else:
            name += key
            stdscr.clear()
            stdscr.addstr(f"Enter your name:{name}", curses.color_pair(1))
            stdscr.refresh()
def overlapping(stdscr,target,user,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM = {wpm}")
    for i,char in enumerate(user):
        coorect_char = target[i]
        color = curses.color_pair(1)
        if char != coorect_char:
            color = curses.color_pair(2)
    
        stdscr.addstr(0, i, char,color)
def random_text():
    a = ["In the golden hues of dawn, dreams take flight.", 
    "Through challenges faced, we rise anew.",
    "Embracing the journey, both old and true.","work hard until you succeed"]
    b = random.choice(a)
    return b

def user_input(stdscr):
    target= random_text()
    user_int=[]
    starting = time.time()
    namee = welcome(stdscr)
    stdscr.nodelay(True)
    while True:
        time_lapse = max(time.time()-starting,1)
        wpm = round(len(user_int)/(time_lapse/60)/5)
        stdscr.clear()
        overlapping(stdscr,target,user_int,wpm)
        stdscr.refresh()
        if "".join(user_int)==target:
            stdscr.nodelay(False) 
            break 
        try:
            key1 = stdscr.getkey()
        except:
            continue
        
        if ord(key1)==27:
            break
        if key1 in ("KEY_BACKSPACE", "\b", "\x7f"):
            user_int.pop()
        elif len(user_int)<=len(target):
            user_int.append(key1)
    
    cursor.execute("SELECT MAX(marks) FROM typing3")
    highest_score = cursor.fetchone()[0]
    if wpm > highest_score:
        # Update the highest score in the table
        update_query = "UPDATE typing3 SET marks = %s, name = %s WHERE id = 1"
        cursor.execute(update_query, (wpm, namee))
        f1.commit()
        stdscr.addstr(3,0,"Congratulations! You have broken the record.")
    else:
        difference = highest_score - wpm
        stdscr.addstr(3,0,f"You need {difference} more wpm to break the record.")

    f1.close()

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    while True:
        user_input(stdscr)
        stdscr.addstr(4,0,"You have completed the game... Press any key to continue..")
        key1 = stdscr.getkey()    
        if ord(key1)==27:
            break
wrapper(main)    