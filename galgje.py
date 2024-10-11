import random

def galgje():
    woorden_lijst = []

    try:
        with open('woorden_galgjer', 'r') as f:
            for line in f:
                woorden_lijst.append(line.strip('\n'))
    except FileNotFoundError:
        print("Het bestand woorden_galgje is niet gevonden.")
        return

    woord = random.choice(woorden_lijst).lower()
    gokken = 10
    gegokt_woord = []
    gegokt_letters = []

    for i in range(len(woord)):
     gegokt_woord.append("_")

    naam = input("Wat is je naam?: ")

    print(f"\nWelkom {naam} bij Galgje!")

    while True:
        print(f"Gegokte letters: [{', '.join(gegokt_letters).upper()}]")
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
            for index, letter in enumerate(woord):
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
            print("Bedankt voor het spelen!")
            break
        else:
            print("Geef antwoord in y of n")