#! python3
# Dependencies - Folium

# poi_mapper.py - CLI-based interface for adding, editing, or removing PoIs
# (points of interest) at a specified location, with automated mapping of PoIs
# onto an interactive map to be stored as HTML file.

import functions_json as fj
import functions_pois as fp
import functions_folium as ff

# Define repeated prompt text for the CLI-based interface
def prompt_default(loc: str):
    print(f'\nCurrent location: {loc}\n'
          'Please select an option:\n'
          '\t1 - Add new point of interest\n'
          '\t2 - View current points of interest\n'
          '\t3 - Edit existing point of interest\n'
          '\t4 - Delete point of interest\n'
          '\t5 - Save and Quit')

# If such data exists, import previously specified location data
info_bound = fj.import_location()

# If such data exists, import previously specified PoI data
pois = fj.import_pois()

toggle_quit = False
while not toggle_quit:
    prompt_default(info_bound['location'])
    response = input()

    # Prompt response to add a new PoI
    if response == '1':
        pois = fp.add_poi(pois)
    
    # Prompt response to view all currently specified PoIs
    elif response == '2':
        fp.view_poi(info_bound['location'], pois)
    
    # Prompt response to edit an existing PoI
    elif response == '3':
        fp.view_poi(info_bound['location'], pois)
        pois = fp.edit_poi(pois)

    # Prompt response to delete a current PoI
    elif response == '4':
        fp.view_poi(info_bound['location'], pois)
        pois = fp.delete_poi(pois)

    # Prompt response to exit out of the PoI Mapper program
    elif response == '5':
        # Export PoI data into an external JSON file for later import
        fj.export_pois(pois)
        # Use specified PoI data to map PoIs onto an interactive map
        map = ff.add_markers(info_bound, pois)
        # Export mapped PoI data into a HTML file
        ff.export_html(map)
        
        # Toggle to exit out of while loop
        toggle_quit = True
        
    else:
        print('Invalid entry, please try again')
