

import funkcije

KARTE_FILE = 'karte.txt'

def str_to_karta(line):
    id, projection_id, price = line.strip().split('|')
    return {
        'id': id,
        'projection_id': projection_id,
        'price': float(price)
    }

def karta_to_str(karta_dict):

    return f"{karta_dict['id']}|{karta_dict['projection_id']}|{karta_dict['price']}"

def save_karte():

    funkcije.save_data(KARTE_FILE, karte, karta_to_str)

def sell_ticket(projekcije_list, projection_id, price):

    projection = funkcije.find_by_id(projekcije_list, projection_id)
    if projection and projection['available_seats'] > 0:

        projection['available_seats'] -= 1
        

        new_ticket = {
            'id': funkcije.generate_next_id(karte, 'K'),
            'projection_id': projection_id,
            'price': float(price)
        }
        

        karte.append(new_ticket)
        save_karte()
        return True, projekcije_list
    
    return False, projekcije_list

def list_karte(karte_list, filmovi_list, projekcije_list):
    if not karte_list:
        print("Nema karata za prikaz.")
        return

    headers = [('ID', 5), ('Film', 20), ('Datum & Vreme', 20), ('Sala', 5), ('Red', 5), ('Sedište', 7), ('Cena', 5)]
    keys_order = ['id', 'film', 'datum_vreme', 'sala', 'red', 'sediste', 'cena']
    
    print(funkcije.format_header(headers))
    
    for karta in karte_list:
        temp_dict = {
            'id': karta['id'],
            'red': karta.get('red', ''),
            'sediste': karta.get('sediste', ''),
            'cena': karta['price']
        }

        projekcija = funkcije.find_by_id(projekcije_list, karta['projection_id'])
        if projekcija:

            temp_dict['datum_vreme'] = f"{projekcija['date']} {projekcija['time']}"
            temp_dict['sala'] = projekcija['hall']
            

            film = funkcije.find_by_id(filmovi_list, projekcija['film_id'])
            if film:
                temp_dict['film'] = film['title']
            else:
                temp_dict['film'] = 'Nepoznat film'
        else:
            temp_dict['datum_vreme'] = ''
            temp_dict['sala'] = ''
            temp_dict['film'] = 'Nepoznat film'
        
        print(funkcije.format_row(temp_dict, keys_order, [width for _, width in headers]))

def list_karte_po_filmu_i_projekciji(karte_list, filmovi_list, projekcije_list):
    print("\nFiltriraj karte po:")
    print("1 - Naslovu filma")
    print("2 - ID projekcije")
    choice = input("Unesite izbor (1-2): ")
    
    filtered_karte = []
    
    if choice == "1":
        title = input("Unesite naslov filma: ")
        

        found_film = None
        for film in filmovi_list:
            if film['title'].lower() == title.lower():
                found_film = film
                break
        
        if found_film:

            film_projections = [p for p in projekcije_list if p['film_id'] == found_film['id']]
            
            if film_projections:
     
                for karta in karte_list:
                    for projekcija in film_projections:
                        if karta['projection_id'] == projekcija['id']:
                            filtered_karte.append(karta)
                            break
                
                print(f"\nKarte za film '{found_film['title']}':")
                list_karte(filtered_karte, filmovi_list, projekcije_list)
            else:
                print(f"\nNema projekcija za film '{found_film['title']}'.")
        else:
            print(f"\nFilm sa naslovom '{title}' nije pronađen.")
    
    elif choice == "2":
        projection_id = input("Unesite ID projekcije: ")
        

        projekcija = funkcije.find_by_id(projekcije_list, projection_id)
        
        if projekcija:

            for karta in karte_list:
                if karta['projection_id'] == projekcija['id']:
                    filtered_karte.append(karta)
            

            film = funkcije.find_by_id(filmovi_list, projekcija['film_id'])
            film_title = film['title'] if film else "Nepoznat film"
            
            print(f"\nKarte za projekciju {projekcija['id']} ({film_title}, {projekcija['date']} {projekcija['time']}, Sala {projekcija['hall']}):")
            list_karte(filtered_karte, filmovi_list, projekcije_list)
        else:
            print(f"\nProjekcija sa ID '{projection_id}' nije pronađena.")
    
    else:
        print("Neispravan izbor.")

def find_karte_by_projekcija_id(projekcija_id):
    return [karta for karta in karte if karta['projection_id'] == projekcija_id]

karte = funkcije.load_data(KARTE_FILE, str_to_karta)