import funkcije

PROJEKCIJE_FILE = 'projekcije.txt'

def str_to_projekcija(line):

    proj_id, film_id, date, time, hall, available_seats = line.strip().split('|')
    return {
        'id': proj_id,
        'film_id': film_id,
        'date': date,
        'time': time,
        'hall': hall,
        'available_seats': int(available_seats)
    }

def projekcija_to_str(projekcija_dict):

    return f"{projekcija_dict['id']}|{projekcija_dict['film_id']}|{projekcija_dict['date']}|{projekcija_dict['time']}|{projekcija_dict['hall']}|{projekcija_dict['available_seats']}"

def save_projekcije():
    """Save the current list of projections to the file."""
    funkcije.save_data(PROJEKCIJE_FILE, projekcije, projekcija_to_str)

def add_projekcija(projekcija_dict, filmovi_list):


    if not funkcije.find_by_id(filmovi_list, projekcija_dict['film_id']):
        print(f"Greška: Film sa ID {projekcija_dict['film_id']} ne postoji.")
        return False
    

    projekcija_dict['id'] = funkcije.generate_next_id(projekcije, 'P')
    projekcije.append(projekcija_dict)
    save_projekcije()
    return True

def update_projekcija(projekcija_id, new_projekcija_dict):

    for i, projekcija in enumerate(projekcije):
        if projekcija['id'] == projekcija_id:
            projekcije[i] = new_projekcija_dict
            save_projekcije()
            return True
    return False

def delete_projekcija(projekcija_id, karte_list):


    projekcija_index = None
    for i, projekcija in enumerate(projekcije):
        if projekcija['id'] == projekcija_id:
            projekcija_index = i
            break
    
    if projekcija_index is None:
        return False
    

    for karta in karte_list:
        if karta['projection_id'] == projekcija_id:
            print(f"Nije moguće obrisati projekciju {projekcija_id} jer ima prodate karte.")
            return False
    

    projekcije.pop(projekcija_index)
    save_projekcije()
    return True

def list_projekcije():
    """Display all projections in a formatted table."""
    headers = [('ID', 5), ('Film ID', 8), ('Datum', 12), ('Vreme', 7), 
               ('Sala', 8), ('Slobodna mesta', 15)]
    keys_order = ['id', 'film_id', 'date', 'time', 'hall', 'available_seats']
    
    print(funkcije.format_header(headers))
    for projekcija in projekcije:
        print(funkcije.format_row(projekcija, keys_order, [5, 8, 12, 7, 8, 15]))

def list_projekcije_po_filmu(projekcije_list, filmovi_list):

    title = input("Unesite naslov filma: ").strip()
    

    found_film = None
    for film in filmovi_list:
        if film['title'].lower() == title.lower():
            found_film = film
            break
    
    if found_film:
        filtered_projekcije = []
        for projekcija in projekcije_list:
            if projekcija['film_id'] == found_film['id']:
                filtered_projekcije.append(projekcija)
        

        if filtered_projekcije:
            print(f"\nProjekcije za film '{found_film['title']}':")
            headers = [('ID', 5), ('Film ID', 8), ('Datum', 12), ('Vreme', 7), 
                      ('Sala', 8), ('Slobodna mesta', 15)]
            keys_order = ['id', 'film_id', 'date', 'time', 'hall', 'available_seats']
            
            print(funkcije.format_header(headers))
            for projekcija in filtered_projekcije:
                print(funkcije.format_row(projekcija, keys_order, [5, 8, 12, 7, 8, 15]))
        else:
            print(f"Nema projekcija za film '{found_film['title']}'.")
    else:
        print(f"Film sa naslovom '{title}' ne postoji.")

def find_projekcija_by_id(projekcija_id):
    
    return funkcije.find_by_id(projekcije, projekcija_id)

def find_projekcije_by_film_id(film_id):

    return [projekcija for projekcija in projekcije 
            if projekcija['film_id'] == film_id]


projekcije = funkcije.load_data(PROJEKCIJE_FILE, str_to_projekcija)