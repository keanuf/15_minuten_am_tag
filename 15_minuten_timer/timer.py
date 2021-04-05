import time
from datetime import datetime, timedelta
import sys
import curses
import simpleaudio as sa

## Das Skript soll eine Art Timer geben,
# um die täglichen 15 Minunten an etwas zu
# aufruf python timer.py xx xx = Zeit in minuten bis der Timer ablaüft

# SoundFile https://soundbible.com/1531-Temple-Bell.html

def main(screen):
    #screen = curses.initscr()
    minuten_time = int(sys.argv[1]) # minuten die man als commando in der console weitergibt
    start_zeit = datetime.now()
    endzeit = start_zeit + timedelta(seconds=minuten_time)
    wav_obj = sa.WaveObject.from_wave_file("sounds/Temple.wav")

    while True:
        time.sleep(1)
        screen.clear()
        if datetime.now() > endzeit:
            print("Timer wurde erreicht")
            curses.beep()
            curses.endwin()
            play_obj = wav_obj.play()
            play_obj.wait_done()
            break
        else:
            screen.addstr(0, 0, datetime.now().strftime("%H:%M:%S"), curses.A_BOLD)
            #print(datetime.now())
            screen.refresh()


curses.wrapper(main)