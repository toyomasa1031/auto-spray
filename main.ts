basic.forever(function () {
    basic.showIcon(IconNames.Asleep)
    if (pins.analogReadPin(AnalogPin.P1) > 450) {
        basic.showIcon(IconNames.Surprised)
        pins.servoWritePin(AnalogPin.P0, 100)
        basic.pause(500)
        pins.servoWritePin(AnalogPin.P0, 0)
        basic.showIcon(IconNames.Happy)
        basic.showLeds(`
            . . . . .
            . # . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.showIcon(IconNames.Happy)
    } else {
        pins.servoWritePin(AnalogPin.P0, 0)
    }
})
