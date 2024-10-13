import galgje
import nummer_raad_spel

# Hoofmenu waar de speler uit games kan kiezen of de app afsluiten
def hoofdmenu():
    while True:
        try:
            spel_nummer = int(input('\nWelkom bij de mini guessing arcade kies het nummer van de game die je wilt spelen.\n'
                      "0. Exit\n"
                      "1. Nummer raad spel\n"
                      "2. Galgje\n"
                      "Kies het nummer: "))
            if spel_nummer == 0:
                print("Tot ziens!")
                break
            elif spel_nummer == 1:
                nummer_raad_spel.nummer_raad_spel()
            elif spel_nummer == 2:
                galgje.galgje()
            else:
                print("Voer een geldig nummer in.")
        except ValueError:
            print("Voer een geldig nummer in.")

# Hoofdmenu openen
hoofdmenu()
