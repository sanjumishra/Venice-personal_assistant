import os
import re

from playsound import playsound
import eel

from engine.command import speak
from engine.config import ASSISTANT_NAME



#sound function for playing sound
def playAssistantSound():
    music_dir = "front-end\\assets\\audio\\tune.mp3"
    playsound(music_dir)

#click sound for mic button

@eel.expose
def playClickSound():
    music_dir = "front-end\\assets\\audio\\tune.mp3"
    playsound(music_dir)
 


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None