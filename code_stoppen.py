"""
Inventaris van mogelijke stopvoorwaarden bij draaien
naar LINKS
"""

# LDR_links = AnalogIn(board.GP26)
# LDR_rechts = AnalogIn(board.GP27)
# LDR_achter = AnalogIn(board.GP28)

TRAGER = 0.2

# DRAAI 1: vertraag op het einde

crossroads_found = False
lijn_in_het_midden = normalise(LDR_links.value) - normalise(LDR_rechts.value) < 0.1 # dalende flank van de functie

if LDR_links_value > 0.5:
    motor_links.duty_cycle = TRAGER
    motor_links.duty_cycle = TRAGER

if normalise(LDR_links.value) - normalise(LDR_rechts.value) > 0.8: # stijgende flank van de functie
    crossroads_found = True
    
if (crossroads_found and lijn_in_het_midden):
    motor_links.duty_cycle = 0
    motor_links.duty_cycle = 0 


# DRAAI 2: verschil tussen huidige en vorige waarde van LDR_links

crossroads_found = False
if normalise(LDR_links.value) - normalise(LDR_rechts.value) > 0.8: # stijgende flank van de functie
    crossroads_found = True

if (
    crossroads_found 
    and LDR_links.value - PREV_LDR_links.value < 0 # draait misschien te ver door dan
):
    motor_links.duty_cycle = 0
    motor_links.duty_cycle = 0   

# DRAAI 3: crossroads_found en rechts ziet zwart

crossroads_found = False
if normalise(LDR_links.value) - normalise(LDR_rechts.value) > 0.8: # stijgende flank van de functie
    crossroads_found = True

if (
    crossroads_found 
    and LDR_rechts.value > 50
):
    motor_rechts.duty_cyle = 0
    motor_links.duty_cycle = 0

# DRAAI 4: snelle draai

if LDR_links.value > 50:
    motor_links.duty_cycle = 0
    motor_links.duty_cycle = 0  

