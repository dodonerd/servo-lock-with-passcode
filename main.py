def on_button_pressed_a():
    global entered
    if len(entered) < len(combination):
        entered = "" + entered + "A"
        basic.show_leds("""
            . . # . .
            . # . # .
            # # # # #
            # . . . #
            # . . . #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global locked, entered
    if entered == combination:
        # Correct combination sound
        music.play_tone(523, music.beat(BeatFraction.QUARTER))
        music.play_tone(659, music.beat(BeatFraction.QUARTER))
        music.play_tone(784, music.beat(BeatFraction.HALF))
        if locked:
            pins.servo_write_pin(AnalogPin.P0, UNLOCKED_ANGLE)
            locked = False
            basic.show_icon(IconNames.YES)
        else:
            pins.servo_write_pin(AnalogPin.P0, LOCKED_ANGLE)
            locked = True
            basic.show_icon(IconNames.SQUARE)
    else:
        # Incorrect combination sound
        music.play_tone(196, music.beat(BeatFraction.HALF))
        music.play_tone(131, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.NO)
    # Clear the entered combination
    entered = ""
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global entered
    if len(entered) < len(combination):
        entered = "" + entered + "B"
        basic.show_leds("""
            # # # . .
            # . . # .
            # # # . .
            # . . # .
            # # # . .
            """)
input.on_button_pressed(Button.B, on_button_pressed_b)

entered = ""
UNLOCKED_ANGLE = 0
LOCKED_ANGLE = 0
locked = False
combination = ""
combination = "AABA"
locked = True
LOCKED_ANGLE = 20
UNLOCKED_ANGLE = 100
# Start with the box locked
pins.servo_write_pin(AnalogPin.P0, LOCKED_ANGLE)
basic.show_icon(IconNames.SQUARE)