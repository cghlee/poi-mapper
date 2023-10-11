import functions_json as fj
import functions_pois as fp
import functions_folium as ff

def prompt_default():
    print('\nPlease select an option:\n'
          '\t1 - Add new point of interest\n'
          '\t2 - View current points of interest\n'
          '\t3 - Edit existing point of interest\n'
          '\t4 - Delete point of interest\n'
          '\t5 - Quit')

info_bound = fj.import_location()

pois = fj.import_pois()

toggle_quit = False
while not toggle_quit:
    prompt_default()
    response = input()

    if response == '1':
        pois = fp.add_poi(pois)
    
    elif response == '2':
        fp.view_poi(info_bound['location'], pois)
    
    elif response == '3':
        fp.view_poi(info_bound['location'], pois)
        pois = fp.edit_poi(pois)

    elif response == '4':
        fp.view_poi(info_bound['location'], pois)
        pois = fp.delete_poi(pois)

    elif response == '5':
        fj.export_pois(pois)
        map = ff.add_markers(info_bound, pois)
            
        print('Saving mapped points of interest to "index.html"')
        map.save("index.html")
        print('Mapping to "index.html" successful\n')
        
        toggle_quit = True
        
    else:
        print('Invalid entry, please try again')