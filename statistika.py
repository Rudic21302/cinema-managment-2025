import funkcije
import matplotlib.pyplot as plt

def generate_earnings_report(filmovi_list, projekcije_list, karte_list):
    film_stats = {}
    
  
    for ticket in karte_list:
        projekcija = funkcije.find_by_id(projekcije_list, ticket['projection_id'])
        if projekcija:
            film_id = projekcija['film_id']
            film = funkcije.find_by_id(filmovi_list, film_id)
            if film:
                if film_id not in film_stats:
                    film_stats[film_id] = {
                        'naslov': film['title'],
                        'tickets_sold': 0,
                        'total_earnings': 0.0
                    }
                film_stats[film_id]['tickets_sold'] += 1
                film_stats[film_id]['total_earnings'] += ticket['price']
    
    for film in filmovi_list:
        film_id = film['id']
        if film_id not in film_stats:
            film_stats[film_id] = {
                'naslov': film['title'],
                'tickets_sold': 0,
                'total_earnings': 0.0
            }
    
    print("\n--- IZVESTAJ ZARADE FILMOVA ---")
    print("Naslov filma          | Prodato karata | Ukupna zarada")
    print("----------------------+----------------+---------------")
    

    for film_id, stats in film_stats.items():
        naslov = stats['naslov'][:20].ljust(20)  
        tickets = str(stats['tickets_sold']).ljust(14)
        earnings = f"{stats['total_earnings']:.2f}".ljust(15)
        print(f"{naslov} | {tickets} | {earnings}")
    

    movie_titles = [stats['naslov'] for stats in film_stats.values()]
    tickets_sold_counts = [stats['tickets_sold'] for stats in film_stats.values()]
    

    plt.figure(figsize=(10, 6))
    plt.bar(movie_titles, tickets_sold_counts)
    plt.title('Broj prodatih karata po filmu')
    plt.xlabel('Naziv filma')
    plt.ylabel('Broj prodatih karata')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def generate_daily_earnings_report(karte_list, projekcije_list):

    daily_earnings = {}
    

    for karta in karte_list:

        projekcija = funkcije.find_by_id(projekcije_list, karta['projection_id'])
        if projekcija:

            datum = projekcija['date']

            if datum not in daily_earnings:
                daily_earnings[datum] = 0.0
                

            daily_earnings[datum] += karta['price']
    

    sorted_dates = sorted(daily_earnings.keys())
    

    print("\n--- IZVESTAJ DNEVNE ZARADE ---")
    print("Datum          | Ukupna zarada")
    print("--------------+---------------")
    

    for datum in sorted_dates:
        earnings = daily_earnings[datum]
        print(f"{datum} | {earnings:.2f}")
    

    dates = sorted_dates
    earnings = [daily_earnings[datum] for datum in sorted_dates]
    
    plt.figure(figsize=(10, 6))
    plt.bar(dates, earnings)
    plt.title('Ukupna zarada po danu')
    plt.xlabel('Datum')
    plt.ylabel('Zarada')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()