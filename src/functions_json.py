#! python3
# Dependencies - Folium

# functions_json.py - Contains functions relating to the JSON data import and
# export, for overall functionality of poi_mapper.py

import os, json

# Import pre-existing location data from a JSON file, or prompts for location
# data to be inputted by the user if said JSON file does not yet exist
def import_location():
    # If it exists, import location data from a pre-existing JSON file
    if os.path.exists('location.json'):
        with open('location.json', 'r', encoding='UTF-8') as file:
            info_bound = json.load(file)
            file.close()
    # Prompt user for location information to subsequently export to JSON file
    else:
        with open('location.json', 'w', encoding='UTF-8') as file:
            print('Please input map bounding information:')
            bound_name = input('\tName of location: ')
            bound_north = input('\tNorth: ')
            bound_south = input('\tSouth: ')
            bound_east = input('\tEast: ')
            bound_west = input('\tWest: ')

            # Ensure that map bound coordinates are inputted correctly
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

            # Export location data to an external JSON file
            print('Saving location information to "location.json"')
            info_json = json.dumps(info_bound)
            file.write(info_json)
            print('Location information successfully saved')
            file.close()

    return info_bound

# Import pre-existing PoI data from a JSON file, or generate empty PoI
# dictionary if such PoI data has yet to be inputted
def import_pois():
    # If it exists, import PoI data from a pre-existing JSON file
    if os.path.exists('pois.json'):
        with open('pois.json', 'r', encoding='UTF-8') as file:
            pois = json.load(file)
            file.close()
    # Generate empty dictionary to subsequently store PoI data
    else:
        pois = {}

    return pois

# Export PoI data into an external JSON file
def export_pois(pois: dict):
    print('\nSaving point of interest information to "pois.json"')
    with open('pois.json', 'w', encoding='UTF-8') as file:
        json_pois = json.dumps(pois)
        file.write(json_pois)
        print('Successfully saved point of interest information')
        file.close()
