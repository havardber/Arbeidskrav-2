# -*- coding: utf-8 -*-
"""


@author: Havard Bergheim - havard@bergheim.org
"""

# Fødselsår skal oppgis til programmet
# input() bruker vi få inn relevant informasjon, som her er fødselsåret.
# int() gjør at det som oppgis, skrives inn, blir til et tall som brukes i regningen.
alder = int(input('Hvilket år er du født? '))

# Programmet skal kunne svare på hvor gammel den som gir infoen blir/ble i 2024.
# Vi trekker fødselsåret fra 2024 for å finne alderen.
alder_i_2024 = 2024 - alder

# Programmet skal svare (skrive ut) alderen i 2024 tilbake
# f for variabler rett inn i teksten, her: alder_i_2024 . Understreker for at 
# det ikke skal tolkes som avgrensninger i koden.
# {alder_i_2024} byttes med selve verdien når programmet kjøres.
print(f'Du blir {alder_i_2024} år i løpet av 2024.')
