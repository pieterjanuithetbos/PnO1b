# LDR_links = AnalogIn(board.GP26)
# LDR_rechts = AnalogIn(board.GP27)
# LDR_achter = AnalogIn(board.GP28)

while metingnummer < 1000:
    metingnummer += 1
    gemiddelde = LDR_links.value + LDR_rechts.value) / 2
    verschil = LDR_rechts.value - LDR_links.value
    print((metingnummer, LDR_links.value, LDR_rechts.value, LDR_achter.value, verschil, gemiddelde))
    time.sleep(0.1)
