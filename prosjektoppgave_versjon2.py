# -*- coding: utf-8 -*-
"""


@author: havar
"""
# Del a) Vi leser inn data fra Excel-filen og lagrer i arrays
# Vi bruker pandas for å kunne lese Excel-filen og jobbe med dataene
import pandas as pd

# Vi leser her inn Excel-filen "support_uke_24.xlsx".
# Vi plasserer filen i samme mappe som .py-filen.
df = pd.read_excel("support_uke_24.xlsx")

# Vi bruker df.iloc[:, 0].values for å hente alle radene fra første kolonne
# --> .values konverterer til en array vi kan burke for nummeriske oppg
# Kolonne 1: Ukedag – vi lagrer det i variabelen u_dag
u_dag = df.iloc[:, 0].values

# Vi bruker her tilsvarende som over, bare justert for kolonnen
# Kolonne 2: Klokkeslett – lagrer det i variabelen kl_slett
kl_slett = df.iloc[:, 1].values

# Vi bruker igjen som over, justert tilsvarende
# Kolonne 3: Varighet – lagres i variabelen varighet
varighet = df.iloc[:, 2].values

# Vi benyttter samme her, her igjen justert for kolonnen.
# Mange kunder har ikke svart, celler i excel-filen er tomme, vi vil
# derfor få mange nan = not a number når vi kjører filen
# Kolonne 4: Score (vedrørende kundens tilfredshet) – lagres i variabelen score
score = df.iloc[:, 3].values

# Vi skriver ut fordi vi vil sjekke at dataene er hentet ut tilfredsstillende
print("Ukedager:", u_dag)
print("Klokkeslett:", kl_slett)
print("Varighet:", varighet)
print("Score:", score)


# Del b) – Vi finner antall henvendelser for hver av de fem ukedagene. Vi
# lager et søylediagram for å framstille.

# Vi importerer matplotlib.pyplot for å ordne diagram, her: stolpediagram
import matplotlib.pyplot as plt

# Vi lager en pandas-series av variabelen u_dag (som er en array med ukedager).
# Vi konverterer på den måten variabelen til en pandas-series for at vi 
# enklere kan telle antall forekomster med value_counts()
# Det vil si hvor mange ganger hver ukedag forekommer.
ukedag_series = pd.Series(u_dag)

# Tell antall henvendelser for hver ukedag ved å bruke value_counts().
# Dette gir oss et resultat der hver ukedag har et tilhørende antall.
antall_ukedager = ukedag_series.value_counts()

# Vi skriver ut antall henvendelser pr. ukedag i konsollen for å se resultatet.
print("\nDel b) Antall henvendelser pr. ukedag:")
print(antall_ukedager)

# Vi lager et stolpediagram for å vise antall henvendelser pr. ukedag.
# Vi prøver å sette størrelsen slik at diagrammet blir OK å lese.
plt.figure(figsize=(8, 6))

# plt.bar lager et stolpediagram.
# Vi bruker index=ukedagene som x-akse og verdiene=antall henvendelser som y-akse.
plt.bar(antall_ukedager.index, antall_ukedager.values)

# Vi definerer titler og beskrivelser på aksene her.
plt.title("Antall henvendelser pr. ukedag")
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")

# Vi viser her diagrammet på skjermen til den som kjører.
plt.show()


# Del c) – Vi finner den minste og lengste samtaletid for uke 24

# Vi importerer numpy som bibliotek for å kunne finne minimum og maksimum.
import numpy as np

# For at det ikke skal feile, trenger vi først å konvertere variabelen 'varighet' (som er en array med formatet HH:MM:SS)
# til en tidsformat som vi kan sammenligne, dvs beregne med. Vi bruker pd.to_timedelta for dette.
varighet_timedelta = pd.to_timedelta(varighet)

# Vi finner den minste (minimum) samtaletiden ved å bruke .min()
min_samtaletid = varighet_timedelta.min()

# Deretter finner vi den lengste (maksimum) samtaletiden ved å bruke .max()
max_samtaletid = varighet_timedelta.max()

# Vi skriver her ut resultatene med informativ tekst.
print("\nDel c) – Minste og lengste samtaletid for uke 24:")
print("Minste samtaletid:", min_samtaletid)
print("Lengste samtaletid:", max_samtaletid)


# Del e) – Vi beregner antall henvendelser pr. tidsintervall (08-10, 10-12, 12-14, 14-16)
# og lager et kakediagram.

# Vi konverterer det i variabelen 'kl_slett' til objekter for date og time.
# Vi bruker formatet '%H:%M:%S' slik at tidspunktene blir tolket korrekt.
klokkeslett_tid = pd.to_datetime(kl_slett, format='%H:%M:%S', errors='coerce')

# Vi henter ut timen fra de konverterte tidspunktene.
# Siden 'klokkeslett_tid' er en DatetimeIndex, bruker vi .hour direkte uten videre dt.hour
time_values = klokkeslett_tid.hour

# Vi definerer her for å telle antall henvendelser i konkrete tidsintervaller..
def count_interval(lower_bound, upper_bound):
    # Vi teller hvor mange tidspunkter i 'time_values' som er
    # større eller like 'lower_bound' og tilsvarende mindre enn 'upper_bound'.
    count = time_values[(time_values >= lower_bound) & (time_values < upper_bound)].size
    return count

# Vi teller antall henvendelser for hvert tidsintervall slik de er oppgitt:
antall_08_10 = count_interval(8, 10)   # Henvendelser mellom kl. 08 og 10
antall_10_12 = count_interval(10, 12)  # Henvendelser mellom kl. 10 og 12
antall_12_14 = count_interval(12, 14)  # Henvendelser mellom kl. 12 og 14
antall_14_16 = count_interval(14, 16)  # Henvendelser mellom kl. 14 og 16

# Vi skriver ut antall henvendelser for hver tidsperiode - dette igjen for å sjekke at resultatet er OK.
print("\nDel e) Antall henvendelser per tidsintervall:")
print("08-10:", antall_08_10)
print("10-12:", antall_10_12)
print("12-14:", antall_12_14)
print("14-16:", antall_14_16)

# VI lager en liste med tidsintervaller og tilhørende antall for deretter å kunne lage et kakediagram.
tidsintervaller = ['08-10', '10-12', '12-14', '14-16']
antall_per_intervall = [antall_08_10, antall_10_12, antall_12_14, antall_14_16]

# Vi lager et kakediagram  for å vise fordelingen av henvendelser på intervallene
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))  # Her setter vi diagrammets størrelse for at det skal kunne leses OK
plt.pie(antall_per_intervall, labels=tidsintervaller, autopct='%1.1f%%', startangle=90)
plt.title("Fordeling av henvendelser pr. tidsintervall")
plt.axis('equal')  # Vi vil ha det i sirkelform
plt.show()


# Del f) – Vi beregner Net Promoter Score (NPS) for supportavdelingen

# Kundens tilfredshet er registrert som en score fra 1 til 10, der:
#    1–6 betyr at kunden er negativ (vil trolig ikke anbefale MORSE)
#    7–8 betyr at kunden er nøytral
#    9–10 betyr at kunden er positiv (vil trolig anbefale MORSE)
# NPS beregnes som: Prosent positive tilbakemeldinger minus prosent negative tilbakemeldinger.

import numpy as np  # Vi importerer numpy igjen

# Vi filtrerer ut de svarene hvor score er gyldig (ikke NaN)
# Dette er nødvendig fordi mange kunder ikke har gitt tilbakemelding, og de mangler score.
score_valid = score[~np.isnan(score)]

# Vi finner totalt antall gyldige svar
totalt_svar = len(score_valid)

# Vi teller antall negative svar: score mellom 1 og 6 (inkludert)
antall_negative = np.sum((score_valid >= 1) & (score_valid <= 6))

# Vi teller antall positive svar: score 9 eller 10 (inkludert)
antall_positive = np.sum((score_valid >= 9) & (score_valid <= 10))

# Vi beregner prosentandelen negative svar
perc_negative = (antall_negative / totalt_svar) * 100

# Vi beregner prosentandelen positive svar
perc_positive = (antall_positive / totalt_svar) * 100

# Vi beregner deretter NPS: prosent positive minus - prosent negative
NPS = perc_positive - perc_negative

# Vi skriever til slutt ut resultatene med beskrivelser slik at vi kan se hva som ble beregnet.
print("\nDel f) – Net Promoter Score (NPS):")
print("Antall negative tilbakemeldinger:", antall_negative, f"({perc_negative:.1f}%)")
print("Antall positive tilbakemeldinger:", antall_positive, f"({perc_positive:.1f}%)")
print("Supportavdelingens NPS:", f"{NPS:.1f}")
