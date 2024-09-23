import time
import pygame
import pendulum

def alarm():
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)


def set_alarm(target_time):
    while True:
        dt = pendulum.now()
        current_time = dt.strftime('%I:%M:%S %p')
        print(current_time, target_time)
        time.sleep(1)
        if current_time == target_time:
            break


target_time = '07:09:00 PM'
set_alarm(target_time)
alarm()
