import random

def nummer_raad_spel():

    print("Welkom bij het nummer raad spel!")
    gegokte_nummers = []

    # Gebruiker laten kiezen tussen het maximale en minimale nummer
    while True:
        try:
            min_nummer = int(input("Vul het laagste nummer in: "))
            max_nummer = int(input("Vul het hoogste nummer in: "))

            # Als min_nummer lager of gelijk aan max_nummer is
            if min_nummer >= max_nummer:
                print("Het laagste nummer kan niet groter of gelijk zijn aan het hoogste nummer")
                continue

            # Nummer maken die de gebruiker moet gokken
            nummer = random.randint(min_nummer, max_nummer)
            break
        # Als er een verkeerde value wordt ingevuld bijvoorbeeld een string
        except ValueError:
            print("Voer een geldig getal in")

    # Vragen hoeveel gokken de gebruiker wilt
    while True:
        try:
            gokken = int(input("Hoeveel gokken wil je?: "))
            if gokken <= 0:
                print("Het aantal gokken moet minimaal 1 zijn.")
                continue
            break
        # Als er een verkeerde value wordt ingevuld bijvoorbeeld een string
        except ValueError:
            print("Voer een geldig getal in")

    for i in range(gokken):

        # Hoeveel gokken heeft de gebruiker?
        if gokken != 1:
            print("Je hebt " + str(gokken) + " gokken.")
        else:
            print("Je hebt " + str(gokken) + " gok.")
         # Vragen om de gebruikers gok
        while True:
            try:
                gok = int(input("Wat is je gok?: "))
                if gok > max_nummer or gok < min_nummer:
                    print("Je gok moet tussen de " + str(min_nummer) + " en " + str(max_nummer) + " zijn.")
                    continue
                elif gok in gegokte_nummers and len(gegokte_nummers) != 0:
                    print(f"Je gok moet uniek zijn! Gegokte nummers: {gegokte_nummers}")
                    continue
                break
            except ValueError:
                print("Voer een geldig getal in")

        if gok == nummer:
            print("Het nummer was " + str(nummer) + "! Je hebt het goed geraden!")
            break
        elif gokken == 1:
            print("Helaas je hebt het niet kunnen raden het nummer was " + str(nummer))
        else:
            print("Jammer " + str(gok) + " was niet het nummer.")
            gegokte_nummers.append(gok)
            gokken -= 1
    # Vragen of de speler opnieuw wilt spelen
    while True:
        keuze = input("Wil je nog een keer spelen? (y/n): ")
        if keuze.lower() == "y":
            nummer_raad_spel()
            break
        elif keuze.lower() == "n":
            print("Bedankt voor het spelen!")
            #hoofdmenu()
            break
        else:
            print("Geef antwoord in y of n")