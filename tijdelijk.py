from helper import decoreer

def print_aanbieding () :
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    aanbieding = prijzen ["aardbei"]*0.8

    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}"

    reclame_tekst_2 = reclame_tekst [:63]

    reclame_tekst_3 = reclame_tekst_2.upper ()

    reclame_tekst_4 = reclame_tekst_3.split ()

    for el in reclame_tekst_4:
        if len (el) <= 4:
            print (el.lower ())
        
        if len (el) >= 5:
            print (el.upper ())

decoreer ("Aanbieding")
print_aanbieding ()