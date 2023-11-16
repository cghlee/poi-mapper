#! python3
# Dependencies - Folium

# functions_folium.py - Contains functions relating to the Folium module in
# Python, for overall functionality of poi_mapper.py

import folium

# Select an appropriate Folium mapping icon based on type of PoI specified
def select_icon(icon_type: str):
    icon_sight = folium.Icon(color='orange', icon='pushpin')
    icon_food = folium.Icon(color='blue', icon='cutlery')
    icon_drink = folium.Icon(color='red', icon='glass')
    icon_accom = folium.Icon(color='green', icon='home')
    icon_other = folium.Icon(color='purple', icon='info-sign')

    if icon_type == 'sightseeing':
        icon = icon_sight
    elif icon_type == 'food':
        icon = icon_food
    elif icon_type == 'drink':
        icon = icon_drink
    elif icon_type == 'accomodation':
        icon = icon_accom
    else:
        icon = icon_other
    
    return icon

# Use specified location and PoI data to generate a Folium map with PoI markers
def add_markers(info_bound: dict, pois: dict):
    print('\nMapping points of interest to "index.html"')
    # Generate a Folium map based upon provided location data
    lat_avg = (float(info_bound['north']) + float(info_bound['south'])) / 2
    long_avg = (float(info_bound['east']) + float(info_bound['west'])) / 2

    map = folium.Map(location=(lat_avg, long_avg))
    map.fit_bounds([[info_bound['north'], info_bound['west']],
                    [info_bound['south'], info_bound['east']]])
    
    # Map all specified PoIs onto the previously generated Folium map
    for key, value in pois.items():
        icon_curr = select_icon(value['type'])
        
        folium.Marker(location = [value['lat'], value['long']],
                      popup = key,
                      icon=icon_curr
                      ).add_to(map)
    
    return map

# Export Folium map into an external HTML file
def export_html(map):
    print('Saving mapped points of interest to "index.html"')
    map.save("index.html")
    print('Mapping to "index.html" successful\n')
