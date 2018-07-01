# gpiozero_fastest_finger
This a 2 players game which will count the total number of times button been pressed by the 2 players within 1 minute.

## Wiring Diagram
![Wiring on Pi-Top proto+](https://github.com/fongkahchun86/gpiozero_fastest_finger/blob/master/fastest%20finger%20electronic%20diagram.png)

## Usage
Wait for the 5 seconds countdown on the buzzer. The last buzz will be a 1 second long buzz to signify the start of the 60 seconds countdown.

The console will print out "```XX sceonds remaining...```" for every 10 seconds, and every 1 second during the last 5 seconds count down.

The game will end with 3 long beeps to signify game over.

Winner will see 3 blinks on his/her LED. Should there be a draw, both players' LEDs will blink simultaneously.
