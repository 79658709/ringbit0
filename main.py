RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)
basic.show_leds("""
    . . . . .
        # . . . #
        # . . . #
        . # # # .
        . . . . .
""")

def on_forever():
    strip.rotate(1)
    basic.pause(100)
    strip.show()
basic.forever(on_forever)

def on_forever2():
    RingbitCar.freestyle(30, 90)
    basic.pause(1500)
    RingbitCar.freestyle(90, 30)
    basic.pause(1500)
basic.forever(on_forever2)
