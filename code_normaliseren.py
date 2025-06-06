# todo zorg dat microswitch na het indrukken nog als botsingsensor kan dienen
# de bedoeling is dat de functie wordt aangesproken voor de auto begint met rijden
# de functie zou moeten starten wanneer een botsingsensor (welke?) wordt ingedrukt

microswitch = digitalio.DigitalInOut(board.GP0)
microswitch.direction = digitalio.Direction.INPUT

def onderzoek_ondergrond():
    op_knop_gedrukt = False

    min_links = 65535
    min_rechts = 65535
    min_achter = 65535
    max_links = 0
    max_rechts = 0
    max_achter = 0
    while not op_knop_gedrukt:

        time.sleep(0.1)

        # onhou de vorige LDR-waarde:
        prev_LDR_links_value = LDR_links_value
        prev_LDR_rechts_value = LDR_rechts_value
        prev_LDR_achter_value = LDR_achter_value

        # lees een nieuwe waarde uit
        LDR_links_value = LDR_links.value
        LDR_rechts_value = LDR_rechts.value
        LDR_achter_value = LDR_achter.value
        print(
            'linksvoor: %s rechtsvoor: %s achter: %s' %
            (LDR_links_value, LDR_rechts_value, LDR_achter_value)
        )

        # houd de kleinste en grootste waarde bij
        if LDR_links_value > max_links:
            max_links = LDR_links_value
        elif LDR_links_value < min_links:
            min_links = LDR_links_value

        if LDR_rechts_value > max_rechts:
            max_rechts = LDR_rechts_value
        elif LDR_rechts_value < min_rechts:
            min_rechts = LDR_rechts_value

        if LDR_achter_value > max_achter:
            max_achter = LDR_achter_value
        elif LDR_achter_value < min_achter:
            min_achter = LDR_achter_value

        # stop als er op de knop gedrukt wordt
        if microswitch.value == True:
            op_knop_gedrukt = True
            print(
                'max links: %s max rechts: %s max achter: %s min links: %s min rechts: %s min achter: %s' %
                (max_links, max_rechts, max_achter, min_links, min_rechts, min_achter)
            )
        # bereken de procentuele afwijking
        LDR_links_procent = (LDR_links_value - min_links) / (max_links - min_links)
        LDR_rechts_procent = (LDR_rechts_value - min_rechts) / (max_rechts - min_rechts)
        LDR_achter_procent = (LDR_achter_value - min_achter) / (max_achter - min_achter)
        LDR_links_procent, LDR_rechts_procent, LDR_achter_procent
    return max_links, max_rechts, max_achter, min_links, min_rechts, min_achter
