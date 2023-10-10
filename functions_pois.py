def add_poi(pois: dict):
    poi_types = ['sightseeing',
                 'food',
                 'drink',
                 'accomodation',
                 'other'
                 ]

    input_name = input('\nInput name of point of interest: ')
    input_lat = input('Input latitude of point of interest: ')
    input_long = input('Input longitude of point of interest: ')

    print('Input type of point of interest:')
    for i in range(len(poi_types)):
        print(f'\t{str(i + 1)} - {poi_types[i].title()}')
    input_type = input()

    info_poi = {'lat': input_lat,
                'long': input_long,
                'type': poi_types[int(input_type) - 1]
                }
    pois[input_name] = info_poi
    
    return pois

def view_poi(loc: str, pois: dict):
    print(f'\nPoints of interest in {loc}')
    for key, value in pois.items():
        print(f'{key} ({value["type"]})')
        print(f'\tLatitude: {value["lat"]}')
        print(f'\tLongitude: {value["long"]}')