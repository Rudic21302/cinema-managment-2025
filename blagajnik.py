import funkcije

BLAGAJNICI_FILE = 'blagajnici.txt'

def str_to_blagajnik(line):
    username, password = line.strip().split('|')
    return {'username': username, 'password': password}

def blagajnik_to_str(blagajnik_dict):
    return f"{blagajnik_dict['username']}|{blagajnik_dict['password']}"

def save_blagajnici():
    funkcije.save_data(BLAGAJNICI_FILE, blagajnici, blagajnik_to_str)

def login(username, password):
    username = username.strip().lower()
    password = password.strip()
    
    for blagajnik in blagajnici:
        if (blagajnik['username'].lower() == username and 
            blagajnik['password'] == password):
            return True
    return False

def add_blagajnik(blagajnik_dict):
    username = blagajnik_dict['username'].strip().lower()
    for blagajnik in blagajnici:
        if blagajnik['username'].lower() == username:
            return False
    
    blagajnici.append(blagajnik_dict)
    save_blagajnici()
    return True

def update_blagajnik(old_username, new_blagajnik_dict):
    old_username = old_username.strip().lower()
    
    for i, blagajnik in enumerate(blagajnici):
        if blagajnik['username'].lower() == old_username:
            blagajnici[i] = new_blagajnik_dict
            save_blagajnici()
            return True
    return False

def delete_blagajnik(username):
    username = username.strip().lower()
    
    for i, blagajnik in enumerate(blagajnici):
        if blagajnik['username'].lower() == username:
            blagajnici.pop(i)
            save_blagajnici()
            return True
    return False

def list_blagajnici():
    headers = [('Korisničko ime', 20), ('Lozinka', 20)]
    keys_order = ['username', 'password']
    
    print(funkcije.format_header(headers))
    for blagajnik in blagajnici:
        print(funkcije.format_row(blagajnik, keys_order, [20, 20]))

blagajnici = funkcije.load_data(BLAGAJNICI_FILE, str_to_blagajnik)