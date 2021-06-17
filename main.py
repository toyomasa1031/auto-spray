def on_forever():
    basic.show_icon(IconNames.ASLEEP)
    if pins.analog_read_pin(AnalogPin.P1) > 450:
        for index in range(2):
            basic.show_icon(IconNames.SURPRISED)
            pins.servo_write_pin(AnalogPin.P0, 100)
            basic.pause(500)
            pins.servo_write_pin(AnalogPin.P0, 0)
            basic.pause(500)
        basic.clear_screen()
        basic.show_icon(IconNames.HAPPY)
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            # . . . #
            . # # # .
            """)
        basic.show_icon(IconNames.HAPPY)
    else:
        pins.servo_write_pin(AnalogPin.P0, 0)
basic.forever(on_forever)
