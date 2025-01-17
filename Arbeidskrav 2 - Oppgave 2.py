# -*- coding: utf-8 -*-
"""
arbeidskrav 2 -oppgave 2

@author: Haavard Bergheim - havard@bergheim.org
"""

# Her ber vi om at det skrives inn antall elever på festen
# antall_elever er en variabel, den holder på antallet elever som svares tilbake
# understrek i navnet på variabelen fordi vi kan ikke ha mellomrom, da det generelt tolkes som en avgresning i koden
antall_elever = int(input('Skriv inn antall elever: '))

# Beregn antall pizzaer som trengs
# antall_pizzaer er variabelen som hjelper oss med å holde på antall pizzaer som må kjøpes
# Hver pizza kan deles i 4 stykker slik oppgaveteksten oppgir at vi antar,
# hver elev spiser 1/4 pizza.
# Vi vil ha husfred og skal ikke gå tom for pizza: 
# For å sikre at det alltid er nok pizzaer, legges det til 3 før divisjonen.
# Dette er en måte å gjøre at vi alltid runder opp til nærmeste hele pizza,
# fordi man ikke kan kjøpe deler av en pizza i butikken. Vi vil heller ha
# litt for mye enn for lite, så vi runder opp.
# Vi vil ha en output som er lett å lese. Divisjon for heltall // gir en mer
# meningsfull (lettere å lese) output; som 6 istedenfor 6.0, slik hintingen
# i oppgaveteksten antyder.
antall_pizzaer = (antall_elever + 3) // 4  # Divisjon for heltall gir oss et heltall

# Vi skriver ut svaret til skjermen
# Resultatet viser antall pizzaer som må kjøpes
print(f'Du må kjøpe {antall_pizzaer} pizzaer til festen.')

