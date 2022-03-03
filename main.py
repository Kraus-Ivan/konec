radio.set_group(62)
RunComp.set_light_level()
start = 0
stav = 0
vysledek = 0
konec = 0

def on_received_number(receivedNumber):
    global start, vysledek, konec
    music.play_tone(Note.C, music.beat())
    if receivedNumber == 1:
        start = control.millis()
radio.on_received_number(on_received_number)

def on_light_drop():
    global konec, vysledek, start
    konec = control.millis()
    vysledek = konec - start
    basic.show_number(vysledek/1000)
    control.reset()
RunComp.on_light_drop(on_light_drop)

def on_forever():
    console.log_value("start", start)
    console.log_value("konec", konec)
    console.log_value("vysledek", vysledek)
basic.forever(on_forever)