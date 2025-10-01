import blagajnik
import film
import projekcija   
import karta
import funkcije
import statistika
import sys

def main():
    print("Dobrodošli u Bioskop Menadžment Sistem!")

    if not user_login():
        print("Neuspešno prijavljivanje. Izlazak iz programa.")
        sys.exit()

    while True:
        display_main_menu()
        choice = input("Izaberite opciju: ").strip()
        if choice.upper() == 'X':
            print("Doviđenja!")
            break
        handle_menu_choice(choice)

def user_login():
    for attempt in range(3):
        username = input("Unesite korisničko ime: ")
        password = input("Unesite lozinku: ")
        if blagajnik.login(username, password):
            print(f"Uspešno ste se prijavili kao {username}.")
            return True
        else:
            print("Pogrešno korisničko ime ili lozinka. Pokušajte ponovo.")
    return False

def display_main_menu():
    print("\nGlavni Meni:")
    print("1 - Upravljanje Blagajnicima")
    print("2 - Upravljanje Filmovima")
    print("3 - Upravljanje Projekcijama")
    print("4 - Upravljanje Kartama")
    print("5 - Statistika")
    print("X - Izlaz")

def handle_menu_choice(choice):
    if choice == '1':
        blagajnik_submenu()
    elif choice == '2':
        film_submenu()
    elif choice == '3':
        projekcija_submenu()
    elif choice == '4':
        karta_submenu()
    elif choice == '5':
        statistika_submenu()
    else:
        print("Nepoznata opcija. Molimo pokušajte ponovo.")

def blagajnik_submenu():
    while True:
        print("\n--- Meni za Blagajnike ---")
        print("1 - Dodaj Blagajnika")
        print("2 - Izmeni Blagajnika")
        print("3 - Obrisi Blagajnika")
        print("4 - Prikazi Sve Blagajnike")
        print("X - Nazad na Glavni Meni")
        choice = input("Izaberite opciju: ").strip()

        if choice == '1':
            username = input("Unesite korisničko ime: ").strip()
            password = input("Unesite lozinku: ").strip()
            blagajnik.add_blagajnik({'username': username, 'password': password})
        elif choice == '2':
            old_username = input("Unesite korisničko ime za izmenu: ").strip()
            new_username = input("Unesite novo korisničko ime: ").strip()
            new_password = input("Unesite novu lozinku: ").strip()
            blagajnik.update_blagajnik(old_username, {'username': new_username, 'password': new_password})
        elif choice == '3':
            username = input("Unesite korisničko ime za brisanje: ").strip()
            blagajnik.delete_blagajnik(username)
        elif choice == '4':
            blagajnik.list_blagajnici()
        elif choice.upper() == 'X':
            break
        else:
            print("Nepoznata opcija.")

def film_submenu():
    while True:
        print("\n--- Meni za Filmove ---")
        print("1 - Dodaj Film")
        print("2 - Izmeni Film")
        print("3 - Obrisi Film")
        print("4 - Prikazi Sve Filmove")
        print("X - Nazad na Glavni Meni")
        choice = input("Izaberite opciju: ").strip()

        if choice == '1':
            naslov = input("Unesite naslov filma: ").strip()
            zanr = input("Unesite žanr: ").strip()
            try:
                trajanje = int(input("Unesite trajanje filma (minuti): ").strip())
                film.add_film({'title': naslov, 'genre': zanr, 'duration': trajanje})
            except ValueError:
                print("Greška: Trajanje mora biti broj.")
        elif choice == '2':
            film_id = input("Unesite ID filma za izmenu: ").strip().upper()
            new_naslov = input("Unesite novi naslov: ").strip()
            new_zanr = input("Unesite novi žanr: ").strip()
            try:
                new_trajanje = int(input("Unesite novo trajanje (minuti): ").strip())
                film.update_film(film_id, {'title': new_naslov, 'genre': new_zanr, 'duration': new_trajanje})
            except ValueError:
                print("Greška: Trajanje mora biti broj.")
        elif choice == '3':
            film_id = input("Unesite ID filma za brisanje: ").strip().upper()
            film.delete_film(film_id, projekcija.projekcije)
        elif choice == '4':
            film.list_filmovi()
        elif choice.upper() == 'X':
            break
        else:
            print("Nepoznata opcija.")

def projekcija_submenu():
    while True:
        print("\n--- Meni za Projekcije ---")
        print("1 - Dodaj Projekciju")
        print("2 - Izmeni Projekciju")
        print("3 - Obrisi Projekciju")
        print("4 - Prikazi Sve Projekcije")
        print("5 - Prikaz projekcija po filmu")
        print("X - Nazad na Glavni Meni")
        choice = input("Izaberite opciju: ").strip()

        if choice == '1':
            film_id = input("Unesite ID filma za projekciju: ").strip().upper()
            datum = input("Unesite datum (YYYY-MM-DD): ").strip()
            vreme = input("Unesite vreme (HH:MM): ").strip()
            sala = input("Unesite salu: ").strip()
            try:
                broj_sedista = int(input("Unesite broj slobodnih sedišta: ").strip())
                projekcija.add_projekcija({'film_id': film_id, 'date': datum, 'time': vreme, 'hall': sala, 'available_seats': broj_sedista}, film.filmovi)
            except ValueError:
                print("Greška: Broj sedišta mora biti broj.")
        elif choice == '2':
            projekcija_id = input("Unesite ID projekcije za izmenu: ").strip().upper()
            new_datum = input("Unesite novi datum (YYYY-MM-DD): ").strip()
            new_vreme = input("Unesite novo vreme (HH:MM): ").strip()
            new_sala = input("Unesite novu salu: ").strip()
            try:
                new_broj_sedista = int(input("Unesite novi broj slobodnih sedišta: ").strip())
                projekcija.update_projekcija(projekcija_id, {'datum': new_datum, 'vreme': new_vreme, 'sala': new_sala, 'available_seats': new_broj_sedista})
            except ValueError:
                print("Greška: Broj sedišta mora biti broj.")
        elif choice == '3':
            projekcija_id = input("Unesite ID projekcije za brisanje: ").strip().upper()
            projekcija.delete_projekcija(projekcija_id, karta.karte)
        elif choice == '4':
            projekcija.list_projekcije()
        elif choice == '5':
            projekcija.list_projekcije_po_filmu(projekcija.projekcije, film.filmovi)
        elif choice.upper() == 'X':
            break
        else:
            print("Nepoznata opcija.")

def karta_submenu():
    global projekcije
    while True:
        print("\n--- Meni za Karte ---")
        print("1 - Prodaj Kartu")
        print("2 - Prikazi Sve Karte")
        print("5 - Prikaz karata po filmu ili projekciji")
        print("X - Nazad na Glavni Meni")
        choice = input("Izaberite opciju: ").strip()

        if choice == '1':
            projekcija_id = input("Unesite ID projekcije: ").strip().upper()
            try:
                cena = float(input("Unesite cenu karte: ").strip())
                success, updated_projekcije = karta.sell_ticket(projekcija.projekcije, projekcija_id, cena)
                if success:
                    projekcija.projekcije = updated_projekcije
                    projekcija.save_projekcije()
                    print("Karta uspešno prodata.")
                else:
                    print("Greška: Projekcija nije pronađena ili nema slobodnih sedišta.")
            except ValueError:
                print("Greška: Cena mora biti broj.")
        elif choice == '2':
            karta.list_karte(karta.karte, film.filmovi, projekcija.projekcije)
        elif choice == '5':
            karta.list_karte_po_filmu_i_projekciji(karta.karte, film.filmovi, projekcija.projekcije)
        elif choice.upper() == 'X':
            break
        else:
            print("Nepoznata opcija.")

def statistika_submenu():
    while True:
        print("\n--- Meni za Statistiku ---")
        print("1 - Izracunaj zaradu")
        print("2 - Prikaz zarade po danima")
        print("X - Nazad na Glavni Meni")
        choice = input("Izaberite opciju: ").strip()

        if choice == '1':
            try:
                statistika.generate_earnings_report(film.filmovi, projekcija.projekcije, karta.karte)
                print("Izveštaj o zaradi je uspešno generisan.")
            except Exception as e:
                print(f"Greška pri generisanju izveštaja: {e}")
        elif choice == '2':
            try:
                statistika.generate_daily_earnings_report(karta.karte, projekcija.projekcije)
                print("Izveštaj o dnevnoj zaradi je uspešno generisan.")
            except Exception as e:
                print(f"Greška pri generisanju izveštaja: {e}")
        elif choice.upper() == 'X':
            break
        else:
            print("Nepoznata opcija.")

if __name__ == '__main__':
    main()