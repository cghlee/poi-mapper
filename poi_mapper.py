import folium

def prompt_default():
    print('\nPlease select an option:\n'
          '\t1 - Add new point of interest\n'
          '\t2 - View current points of interest\n'
          '\t3 - Quit')
    
print('Please input map bounding information:')
bound_name = input('\tName of location: ')
bound_north = input('\tNorth: ')
bound_south = input('\tSouth: ')
bound_east = input('\tEast: ')
bound_west = input('\tWest: ')

info_bound = {'location': bound_name,
              'north': bound_north,
              'south': bound_south,
              'east': bound_east,
              'west': bound_west
              }

pois = {}
poi_types = ['sightseeing',
             'food',
             'drink',
             'accomodation',
             'other'
             ]

toggle_quit = False
while not toggle_quit:
    prompt_default()
    response = input()

    if response == '1':
        input_name = input('\nInput name of point of interest: ')
        input_lat = input('Input latitude of point of interest: ')
        input_long = input('Input longitude of point of interest: ')

        print('Input type of point of interest:')
        counter_type = 0
        for type in poi_types:
            print(f'\t{str(counter_type + 1)} - {poi_types[counter_type].title()}')
            counter_type += 1
        input_type = input()

        info_poi = {'lat': input_lat,
                    'long': input_long,
                    'type': poi_types[int(input_type) - 1]
                    }
        pois[input_name] = info_poi
    
    elif response == '2':
        print(f'\nPoints of interest in {info_bound["location"]}')
        for key, value in pois.items():
            print(f'{key} ({value["type"]})')
            print(f'\tLatitude: {value["lat"]}')
            print(f'\tLongitude: {value["long"]}')
    
    elif response == '3':
        print('\nMapping points of interest to "index.html"')
        lat_avg = (float(info_bound['north']) + float(info_bound['south'])) / 2
        long_avg = (float(info_bound['east']) + float(info_bound['west'])) / 2

        map = folium.Map(location=(lat_avg, long_avg))
        map.fit_bounds([[info_bound['north'], info_bound['west']],
                        [info_bound['south'], info_bound['east']]])

        icon_sight = folium.Icon(color='orange', icon='pushpin')
        icon_food = folium.Icon(color='blue', icon='cutlery')
        icon_drink = folium.Icon(color='red', icon='glass')
        icon_accom = folium.Icon(color='green', icon='home')
        icon_other = folium.Icon(color='pink', icon='heart')

        for key, value in pois.items():
            if value['type'] == 'sightseeing':
                icon_curr = icon_sight
            elif value['type'] == 'food':
                icon_curr = icon_food
            elif value['type'] == 'drink':
                icon_curr = icon_drink
            elif value['type'] == 'accomodation':
                icon_curr = icon_accom
            else:
                icon_curr = icon_other
            
            folium.Marker(location = [value['lat'], value['long']],
                          popup = key,
                          icon=icon_curr
                          ).add_to(map)
            
        print('Saving mapped points of interest to "index.html"')
        map.save("index.html")
        print('Mapping to "index.html" successful\n')
        
        toggle_quit = True
        
    else:
        print('Please input a valid response')