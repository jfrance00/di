# Exercise 1
def combine_lists():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    combo = dict(zip(keys, values))
    print(combo)


def create_store():
    store = {
        'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H & M', 'Benetton'],
        'number_stores': 7000,
        'major_color': {'France' : 'blue', 'Spain' : 'red', 'US' : ['pink', 'green']},
        }
    store['number_stores'] = 2
    store['country_creation'] = 'Spain'
    del store['creation_date']
    intl_competitor = store.get('international_competitors')
    last_international_competitor = intl_competitor[len(intl_competitor)-1]
    color = store.get('major_color')
    print("The major colors of the US are {} and {}".format(color['US'][0],color['US'][1]))
    print(len(store))
    print(store.keys())

    more_on_store = store
    more_on_store["creation_date"] = 1975
    more_on_store["number_stores"] = 10000
    print(more_on_store)
    print("store: {}".format(store))
    return store

store = create_store()

def add_store(store, country, number):
    if("stores_worldwide" in store.keys()):
        store['stores_worldwide'] = {
                                    'country' : country,
                                    'number' : number,
                                     }
        
    else:
        store['stores_worldwide'] = {}
add_store(store, 'country', 'number')
print(store)