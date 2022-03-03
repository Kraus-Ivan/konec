radio.setGroup(62)
RunComp.SetLightLevel()
let start = 0
let stav = 0
let vysledek = 0
let konec = 0
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    music.playTone(Note.C, music.beat())
    if (receivedNumber == 1) {
        start = control.millis()
    }
    
})
RunComp.OnLightDrop(function on_light_drop() {
    
    konec = control.millis()
    vysledek = konec - start
    basic.showNumber(vysledek / 1000)
    control.reset()
})
basic.forever(function on_forever() {
    console.logValue("start", start)
    console.logValue("konec", konec)
    console.logValue("vysledek", vysledek)
})
