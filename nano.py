import random

def nummer_raad_spel():

    print("Welkom bij het nummer raad spel!")

    # Gebruiker laten kiezen tussen het maximale en minimale nummer
    while True:
        try:
            min_nummer = int(input("Vul het laagste nummer in: "))
            max_nummer = int(input("Vul het hoogste nummer in: "))

            # Als min_nummer lager of gelijk aan max_nummer is
            if min_nummer >= max_nummer:
                print("Het laagste kan niet groter of gelijk zijn aan het hoogste nummer")
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
            gokken -= 1
    # Vragen of de speler opnieuw wilt spelen
    while True:
        keuze = input("Wil je nog een keer spelen? (y/n): ")
        if keuze.lower() == "y":
            nummer_raad_spel()
            break
        elif keuze.lower() == "n":
            hoofdmenu()
            break
        else:
            print("Geef antwoord in y of n")

# Hoofmenu waar de speler uit games kan kiezen of de app afsluiten
def hoofdmenu():
    while True:
        try:
            spel_nummer = int(input('\nWelkom bij Nano kies het nummer van de game die je wilt spelen.\n'
                      "0. Exit\n"
                      "1. Nummer raad spel\n"
                      "2. Galgje\n"
                      "Kies het nummer: "))
            if spel_nummer == 0:
                print("Tot ziens!")
                break
            elif spel_nummer == 1:
                nummer_raad_spel()
                break
            elif spel_nummer == 2:
                galgje()
                break
            else:
                print("Voer een geldig nummer in.")
        except ValueError:
            print("Voer een geldig nummer in.")

def galgje():
    woorden_lijst = ["Appel", "Auto", "Laptop"]
    woord = random.choice(woorden_lijst).lower()
    gokken = 10
    gegokt_woord = []
    gegokt_letters = []

    for i in range(len(woord)):
     gegokt_woord.append("_")

    print("\nWelkom bij Galgje!")

    while True:
        print(f"Woord: {' '.join(gegokt_woord)}")
        if gokken != 1:
            print(f"Je hebt nog {gokken} gokken om het te raden.")
        else:
            print(f"Je hebt nog {gokken} gok!")

        gok = str(input("Maak een gok: ")).lower()

        while len(gok) != 1 or not gok.isalpha() or gok in gegokt_letters:
            gok = str(input("Voer een geldige letter in je nog niet hebt gegokt: "))
            continue

        gegokt_letters.append(gok)

        if gok in woord:
            print(f"\n{gok} Zit in het woord")
            for index, letter in enumerate(woord): #TODO: check this
                if letter == gok:
                    gegokt_woord[index] = gok
        else:
            print(f"\n{gok} Zit niet in het woord")
            gokken -= 1

        if "_" not in gegokt_woord:
            print("Gefeliciteerd! Je hebt het woord geraden!")
            break
        elif gokken <= 0:
            print(f"Je hebt verloren! Het woord was: {woord}")
            break

    while True:
        keuze = input("Wil je nog een keer spelen? (y/n): ")
        if keuze.lower() == "y":
            galgje()
            break
        elif keuze.lower() == "n":
            hoofdmenu()
            break
        else:
            print("Geef antwoord in y of n")

# Hoofdmenu openen
hoofdmenu()
