input.onButtonPressed(Button.A, function () {
    if (entered.length < combination.length) {
        entered = "" + entered + "A"
        basic.showLeds(`
            . . # . .
            . # . # .
            # # # # #
            # . . . #
            # . . . #
            `)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (entered == combination) {
        // Correct combination sound
        music.playTone(523, music.beat(BeatFraction.Quarter))
        music.playTone(659, music.beat(BeatFraction.Quarter))
        music.playTone(784, music.beat(BeatFraction.Half))
        if (locked) {
            pins.servoWritePin(AnalogPin.P0, UNLOCKED_ANGLE)
            locked = false
            basic.showIcon(IconNames.Yes)
        } else {
            pins.servoWritePin(AnalogPin.P0, LOCKED_ANGLE)
            locked = true
            basic.showIcon(IconNames.Square)
        }
    } else {
        // Incorrect combination sound
        music.playTone(196, music.beat(BeatFraction.Half))
        music.playTone(131, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.No)
    }
    // Clear the entered combination
    entered = ""
    basic.pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (entered.length < combination.length) {
        entered = "" + entered + "B"
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # . .
            # . . # .
            # # # . .
            `)
    }
})
let entered = ""
let UNLOCKED_ANGLE = 0
let LOCKED_ANGLE = 0
let locked = false
let combination = ""
combination = "AABA"
locked = true
LOCKED_ANGLE = 20
UNLOCKED_ANGLE = 100
// Start with the box locked
pins.servoWritePin(AnalogPin.P0, LOCKED_ANGLE)
basic.showIcon(IconNames.Square)
