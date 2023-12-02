# Song Data
from typing import Tuple

hot_cross_buns = [("E", 3), ("D", 2), ("C", 1), ("E", 3), ("D", 2), ("C", 1), ("C", 1), ("C", 1), ("C", 1), ("C", 1),
                  ("D", 2), ("D", 2), ("D", 2), ("D", 2), ("E", 3), ("D", 2), ("C", 1)]


####################################################

def collect_press() -> int:
    """Detecting if any finger has been pressed, returns 0 if none has been pressed"""
    # TODO: figure out how to define this
    # WARNING: make sure this doesn't get confused when multiple sensors are pressed at once

def collect_song() -> str:
    """Determine which song the user wants to play through finger presses"""
    # TODO: detect what song through pressure
    return hot_cross_buns

def set_main_led(bool: bool) -> None:
    """Update main LED so that user knows they selected the wrong note"""
    if bool:
        #set green
    else:
        #set red
    # TODO: figure out how to update led
    return None

def play_tone(key: str) -> None:
    return None

def get_rbd_reading() -> int:
    """Retrieve value from color sensor being selected"""
    # Maybe create a map of color sensors to pressure sensors so you know which one to read.
    return 0

def set_finger_led(note: Tuple[str, int]) -> None:
    """Update LED finger with color representing the note that should be pressed"""
    return None

def loop():

    # user must select song to start the process
    song = collect_song()

    for note in song:
        # TODO: light up finger with specific color
        set_finger_led(note) # make this setting optional when starting song for range of difficulty?

        while collect_press() != note(1):
            if collect_press() != 0: # If a press is made and it's not the correct one...
                set_main_led(False)

        set_main_led(True)
        play_tone(note(0), get_rbd_reading()) # TODO: figure out whether to use fixed or color value


