from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - (prijs*korting)} euro. "

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(*inkomsten):
    totaal = sum(inkomsten)
    bedrag = sum(inkomsten)*0.09
    week_totaal = f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarvoor {bedrag:.2f} euro btw betaald dient te worden."
    return week_totaal

print(inkomsten_totaal(220, 430, 125, 160, 205, 90, 345))

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

print(laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    week_gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    gemiddelde_week = f"De gemiddelde inkomsten deze week zijn {week_gemiddelde:.2f} euro."
    return gemiddelde_week

print(gemiddelde(mijn_lijst))

def meervoudig(*invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print (meervoudig(10, 5, 3, 2, 1 ,2, 9))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2 (korte_lijst[0], korte_lijst[1])
    return uitvoer