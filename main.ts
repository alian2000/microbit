input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.SmallSquare)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Heart)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("Usama Alian")
})
