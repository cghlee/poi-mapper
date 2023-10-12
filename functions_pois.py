poi_types = ['sightseeing',
             'food',
             'drink',
             'accomodation',
             'other'
             ]

def view_poi_types():
    for i in range(len(poi_types)):
        print(f'\t{str(i + 1)} - {poi_types[i].title()}')

def pull_poi_type(type_num: str):
    type_str = poi_types[int(type_num) - 1]
    return type_str

def add_poi(pois: dict):
    input_name = input('\nInput name of point of interest: ')
    input_lat = input('Input latitude (or with longitude, separated by comma): ')
    if ',' in input_lat:
        coord_split = input_lat.split(',')
        input_lat = coord_split[0].strip()
        input_long = coord_split[1].strip()
    else:
        input_long = input('Input longitude: ')

    print('Input type of point of interest:')
    view_poi_types()
    input_type = input()
    type_str = pull_poi_type(input_type)

    info_poi = {'lat': input_lat,
                'long': input_long,
                'type': type_str
                }
    pois[input_name] = info_poi
    print(f'{input_name} successfully added')
    
    return pois

def view_poi(loc: str, pois: dict):
    print(f'\nPoints of interest in {loc}:')
    pois_sorted = sorted(pois.items())
    for i in range(len(pois_sorted)):
        print(f'({i + 1}) {pois_sorted[i][0]} ({pois_sorted[i][1]["type"]})')
        print(f'\tLatitude: {pois_sorted[i][1]["lat"]}')
        print(f'\tLongitude: {pois_sorted[i][1]["long"]}')

def edit_poi(pois: dict):
    edit_num = input('\nEnter number of point of interest to edit: ')
    edit_key = sorted(pois)[int(edit_num) - 1]

    print(f'\nSelect variable to change for "{edit_key}":\n'
            '\t1 - Name\n'
            '\t2 - Latitude\n'
            '\t3 - Longitude\n'
            '\t4 - Type')
    edit_variable = input()

    if edit_variable == '1':
        name_new = input(f'Enter new name for "{edit_key}": ')
        pois[name_new] = pois[edit_key]
        del pois[edit_key]
        print('Name successfully changed')

    elif edit_variable == '2':
        lat_new = input(f'Enter new latitude value for "{edit_key}": ')
        pois[edit_key]['lat'] = lat_new
        print('Latitude successfully changed')

    elif edit_variable == '3':
        long_new = input(f'Enter new longitude value for "{edit_key}": ')
        pois[edit_key]['long'] = long_new
        print('Longitude successfully changed')

    elif edit_variable == '4':
        print(f'Enter new type of point of interest for "{edit_key}": ')
        view_poi_types()
        type_new = input()
        type_str = pull_poi_type(type_new)
        pois[edit_key]['type'] = type_str
        print('Type successfully changed')
    
    else:
        print('Invalid entry, please try again')
    
    return pois

def delete_poi(pois: dict):
    del_num = input('\nEnter number of point of interest to delete: ')
    del_key = sorted(pois)[int(del_num) - 1]

    del pois[del_key]
    print(f'Listing for "{del_key}" successfully deleted')

    return pois