def on_button_pressed_a():
    for value in ["ali", "bader", "Charlie"]:
        basic.show_string("Name= " + str((["a", "b", "C"])))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("Usama Alian")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
