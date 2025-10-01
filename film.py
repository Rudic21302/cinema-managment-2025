import funkcije

FILMOVI_FILE = 'filmovi.txt'

def str_to_film(line):
    film_id, title, genre, duration = line.strip().split('|')
    return {
        'id': film_id,
        'title': title,
        'genre': genre,
        'duration': int(duration)
    }

def film_to_str(film_dict):
    return f"{film_dict['id']}|{film_dict['title']}|{film_dict['genre']}|{film_dict['duration']}"

def save_filmovi():
    funkcije.save_data(FILMOVI_FILE, filmovi, film_to_str)

def add_film(film_dict):
    for film in filmovi:
        if film['title'].lower() == film_dict['title'].lower():
            return False
    
    film_dict['id'] = funkcije.generate_next_id(filmovi, 'F')
    filmovi.append(film_dict)
    save_filmovi()
    return True

def update_film(film_id, new_film_dict):
    for i, film in enumerate(filmovi):
        if film['id'] == film_id:
            filmovi[i] = new_film_dict
            save_filmovi()
            return True
    return False

def delete_film(film_id, projekcije_list):
    film_index = None
    for i, film in enumerate(filmovi):
        if film['id'] == film_id:
            film_index = i
            break
    
    if film_index is None:
        return False
    
    for projekcija in projekcije_list:
        if projekcija['film_id'] == film_id:
            print(f"Nije moguće obrisati film {film_id} jer ima zakazane projekcije.")
            return False
    
    filmovi.pop(film_index)
    save_filmovi()
    return True

def list_filmovi():
    headers = [('ID', 5), ('Naslov', 25), ('Žanr', 15), ('Trajanje (min)', 15)]
    keys_order = ['id', 'title', 'genre', 'duration']
    
    print(funkcije.format_header(headers))
    for film in filmovi:
        print(funkcije.format_row(film, keys_order, [5, 25, 15, 15]))

def find_film_by_id(film_id):
    return funkcije.find_by_id(filmovi, film_id)

filmovi = funkcije.load_data(FILMOVI_FILE, str_to_film)