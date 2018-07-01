"""
This is a 2 players game which will count the total number of times both buttons are pressed
by the 2 players.
The buzzer will count down 5 secs before the game start with a short beep. The game will end 60
seconds later with 3 long beep. Total scores will be display on the console.
"""

from gpiozero import LED, Buzzer, Button
from random import choice
from time import sleep
from signal import pause
import threading

led_r = LED(4)
led_g = LED(5)
bn_left = Button(27)
bn_right = Button(13)
bz = Buzzer(17)

player1_score, player2_score = 0, 0
game_duration = 60 #in seconds

def bn_left_pressed():
    led_r.on()

def bn_right_pressed():
    led_g.on()

def bn_left_released():
    led_r.off()
    global player1_score
    player1_score += 1

def bn_right_released():
    led_g.off()
    global player2_score
    player2_score += 1

bn_left.when_pressed = bn_left_pressed
bn_left.when_released = bn_left_released
bn_right.when_pressed = bn_right_pressed
bn_right.when_released = bn_right_released

#5 secs buzzer countdown
for i in range(4):
    bz.on()
    sleep(0.5)
    bz.off()
    sleep(0.5)
bz.on() #Long beep to signal the start
sleep(1)
bz.off()

countdown_reminder = [60, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1]

while game_duration > 0:
    sleep(1)
    if game_duration in countdown_reminder:
        print(game_duration, "seconds remaining...")
    game_duration -= 1

print("Game over!")
#Ending 3 long beeps
for i in range(3):
    bz.on()
    sleep(0.8)
    bz.off()
    sleep(0.2)
    
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
if player1_score > player2_score:
    led_r.blink(on_time = 0.8, off_time = 0.2, n = 3)
    print("Player 1 wins!")
elif player2_score > player1_score:
    led_g.blink(on_time = 0.8, off_time = 0.2, n = 3)
    print("Player 2 wins!")
else:
    led_r.blink(on_time = 0.8, off_time = 0.2, n = 3)
    led_g.blink(on_time = 0.8, off_time = 0.2, n = 3)
    print("It's a draw!")

pause()
