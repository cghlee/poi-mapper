#! python3
# Dependencies - Folium

# functions_pois.py - Contains functions relating to manulation of PoI (point
# of interest) data, for overall functionality of poi_mapper.py

# Specify types of PoI recognised by the PoI Mapper
poi_types = ['sightseeing',
             'food',
             'drink',
             'accomodation',
             'other'
             ]

# View specified types of PoI in numbered list format
def view_poi_types():
    for i in range(len(poi_types)):
        print(f'\t{str(i + 1)} - {poi_types[i].title()}')

# Return type of PoI in string format based on the previous numbered list
def pull_poi_type(type_num: str):
    type_str = poi_types[int(type_num) - 1]
    return type_str

# Add new PoI to dictionary using prompted information
def add_poi(pois: dict):
    input_name = input('\nInput name of point of interest: ')
    # Allow simultaneous input of latitude and longitude input, if desired
    input_lat = input('Input latitude (or with longitude, separated by comma): ')
    if ',' in input_lat:
        coord_split = input_lat.split(',')
        input_lat = coord_split[0].strip()
        input_long = coord_split[1].strip()
    else:
        input_long = input('Input longitude: ')

    # Prompt for type of PoI being added
    print('Input type of point of interest:')
    view_poi_types()
    input_type = input()
    type_str = pull_poi_type(input_type)

    # Store non-name PoI data in nested dictionary format
    info_poi = {'lat': input_lat,
                'long': input_long,
                'type': type_str
                }
    pois[input_name] = info_poi
    print(f'{input_name} successfully added')
    
    return pois

# View all currently specified PoIs in numbered list format
def view_poi(loc: str, pois: dict):
    print(f'\nPoints of interest in {loc}:')
    pois_sorted = sorted(pois.items())
    for i in range(len(pois_sorted)):
        print(f'({i + 1}) {pois_sorted[i][0]} ({pois_sorted[i][1]["type"]})')
        print(f'\tLatitude: {pois_sorted[i][1]["lat"]}')
        print(f'\tLongitude: {pois_sorted[i][1]["long"]}')

# Edit data for a current PoI
def edit_poi(pois: dict):
    # Specify a specific PoI via designation using the previous numbered list
    edit_num = input('\nEnter number of point of interest to edit: ')
    edit_key = sorted(pois)[int(edit_num) - 1]

    # Prompt for PoI data to be edited
    print(f'\nSelect variable to change for "{edit_key}":\n'
            '\t1 - Name\n'
            '\t2 - Latitude\n'
            '\t3 - Longitude\n'
            '\t4 - Type')
    edit_variable = input()

    # Prompt response to edit name (key) of designated PoI
    if edit_variable == '1':
        name_new = input(f'Enter new name for "{edit_key}": ')
        pois[name_new] = pois[edit_key]
        del pois[edit_key]
        print('Name successfully changed')

    # Prompt response to edit latitude value of designated PoI
    elif edit_variable == '2':
        lat_new = input(f'Enter new latitude value for "{edit_key}": ')
        pois[edit_key]['lat'] = lat_new
        print('Latitude successfully changed')

    # Prompt response to edit longitude value of designated PoI
    elif edit_variable == '3':
        long_new = input(f'Enter new longitude value for "{edit_key}": ')
        pois[edit_key]['long'] = long_new
        print('Longitude successfully changed')

    # Prompt response to edit type of PoI for the designated PoI
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

# Delete existing PoI via designation using the previous numbered list
def delete_poi(pois: dict):
    del_num = input('\nEnter number of point of interest to delete: ')
    del_key = sorted(pois)[int(del_num) - 1]

    del pois[del_key]
    print(f'Listing for "{del_key}" successfully deleted')

    return pois
