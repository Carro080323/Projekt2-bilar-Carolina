'''
FILNAMN.PY: Bilhantering – lista med bilar

__author__  = "Carolina Hedberg"
__version__ = "1.0.0"
__email__   = "carolina.hedberg@elev.ga.ntig.se"
'''

import os
os.system('cls')

from bcolors import bcolors

# Beskrivning:
# Detta program låter användaren hantera en lista med bilar.
# Man kan lägga till, ta bort, ändra namn på bilar och visa hela listan.
# Programmet går att avsluta manuellt med "/q" eller genom att lämna input tom.


# Funktion som skriver ut bilarna snyggt vid start

def print_start_cars(car_list):
    """Skriver ut bilarna snyggt när programmet startar."""
    print("-" * 30)

    if car_list:
        for i, car in enumerate(car_list, start=1):
            print(f"{i}. {car}")
    else:
        print("Inga bilar finns ännu.")

    print("-" * 30)


# Lista som ska lagra bilar

cars_list = ["ferrari 256", "porche"]


# Funktion för att lägga till en bil

def add_car(lista, car):
    """Lägger till en bil i listan om den inte redan finns."""
    if car in lista:
        print(f"{car} finns redan i listan.")
    else:
        lista.append(car)
        print(f"{car} har lagts till.")


# Funktion för att ta bort en bil

def remove_car(lista, car):
    """Tar bort en bil från listan om den finns."""
    if car in lista:
        lista.remove(car)
        print(f"{car} har tagits bort.")
    else:
        print(f"{car} finns inte i listan.")


# Funktion för att ändra en bil

def change_car(lista, old_car, new_car):
    """Byter namn på en bil i listan."""
    if old_car in lista:
        index = lista.index(old_car)
        lista[index] = new_car
        print(f"{old_car} har ändrats till {new_car}.")
    else:
        print(f"{old_car} finns inte i listan.")


# Funktion för att visa alla bilar

def show_cars(lista):
    """Visar alla bilar i listan."""
    if lista:
        print("Bilar i listan:")
        for i, car in enumerate(lista, start=1):
            print(f"{i}. {car}")
    else:
        print("Listan är tom.")


# Programstart – rubrik + antal + lista

print(bcolors.YELLOW + "=== MINA FAVVOBILAR I GARAGET 🚗 ===")
print(f"Totalt antal bilar i garaget: {len(cars_list)}")
print(bcolors.DEFAULT)
print_start_cars(cars_list)


# Huvudprogram

while True:
    print(bcolors.YELLOW + "\n--- Bilhantering ---")
    print(bcolors.DEFAULT)
    print("1. Lägg till bil")
    print("2. Ta bort bil")
    print("3. Ändra bil")
    print("4. Visa alla bilar")
    print("5. Avsluta programmet")

    choice = input(bcolors.GREEN + "Välj ett alternativ (1-5, eller '/q' för att avsluta): ").strip()
    print(bcolors.DEFAULT)

    # Avsluta programmet
    if choice.lower() == "/q" or choice == "5":
        print(bcolors.RED + f"Program avslutas. Totalt antal bilar i listan: {len(cars_list)}")
        print(bcolors.DEFAULT)
        break

    # Lägg till bil
    elif choice == "1":
        car_name = input("Skriv namnet på bilen att lägga till (eller '/q' för att avsluta): ").strip()
        if car_name == "" or car_name.lower() == "/q":
            continue
        add_car(cars_list, car_name)

    # Ta bort bil
    elif choice == "2":
        car_name = input("Skriv namnet på bilen att ta bort (eller '/q' för att avsluta): ").strip()
        if car_name == "" or car_name.lower() == "/q":
            continue
        remove_car(cars_list, car_name)

    # Ändra bil
    elif choice == "3":
        old_car = input("Vilken bil vill du ändra? (eller '/q' för att avsluta): ").strip()
        if old_car == "" or old_car.lower() == "/q":
            continue

        new_car = input("Nytt namn på bilen: ").strip()
        if new_car == "" or new_car.lower() == "/q":
            continue

        change_car(cars_list, old_car, new_car)

    # Visa alla bilar
    elif choice == "4":
        show_cars(cars_list)

    else:
        print("Ogiltigt val. Välj 1–5 eller '/q'.")