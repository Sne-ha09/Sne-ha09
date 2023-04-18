from playsound import playsound
from time import sleep

from gtts import gTTS

greeting= gTTS(" Hello.")
greeting.save (" Hello.mp3")

greeting_again= gTTS("Nice to meet you.")
greeting_again.save ("Nice to meet you.mp3")

playsound("greeting.mp3") 
sleep(1)
playsound("greeting_again.mp3")
