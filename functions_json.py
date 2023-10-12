import os, json

def import_location():
    if os.path.exists('location.json'):
        with open('location.json', 'r', encoding='UTF-8') as file:
            info_bound = json.load(file)
            file.close()
    else:
        with open('location.json', 'w', encoding='UTF-8') as file:
            print('Please input map bounding information:')
            bound_name = input('\tName of location: ')
            bound_north = input('\tNorth: ')
            bound_south = input('\tSouth: ')
            bound_east = input('\tEast: ')
            bound_west = input('\tWest: ')

            if float(bound_north) < float(bound_south):
                bound_north, bound_south = bound_south, bound_north
            if float(bound_east) < float(bound_west):
                bound_east, bound_west = bound_west, bound_east

            info_bound = {'location': bound_name,
                        'north': bound_north,
                        'south': bound_south,
                        'east': bound_east,
                        'west': bound_west
                        }

            print('Saving location information to "location.json"')
            info_json = json.dumps(info_bound)
            file.write(info_json)
            print('Location information successfully saved')
            file.close()

    return info_bound

def import_pois():
    if os.path.exists('pois.json'):
        with open('pois.json', 'r', encoding='UTF-8') as file:
            pois = json.load(file)
            file.close()
    else:
        pois = {}

    return pois

def export_pois(pois: dict):
    print('\nSaving point of interest information to "pois.json"')
    with open('pois.json', 'w', encoding='UTF-8') as file:
        json_pois = json.dumps(pois)
        file.write(json_pois)
        print('Successfully saved point of interest information')
        file.close()